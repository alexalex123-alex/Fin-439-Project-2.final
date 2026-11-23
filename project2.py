"""Northbridge research engine. Decimal rates; standard library only."""
import copy
import csv
import hashlib
import json
from datetime import date
from pathlib import Path
import portfolio as p

ROOT = Path(__file__).resolve().parent
TICKERS = ['BIL', 'IEF', 'LQD', 'VT']
DEFAULTS = dict(target=.055, reserve=.03, risk_limit=.08, cost_bps=25.,
                equity_haircut=0., last_36=False, turnover_limit=.20)
CURRENT = [.70, 0., 0., .30]  # hypothetical starting holdings, NOT an account statement


def evaluate(weights, assets, correlations, cfg):
    gross = p.expected_return(weights, assets)
    vol = p.portfolio_volatility(weights, p.covariance_matrix(assets, correlations))
    net = gross - cfg['cost_bps'] / 10000
    turnover = sum(abs(a-b) for a,b in zip(weights, CURRENT)) / 2
    rules = {
        'fully funded / long only': abs(sum(weights)-1) < 1e-10 and min(weights) >= 0,
        'net return proxy >= target': net + 1e-12 >= cfg['target'],
        'BIL reserve >= minimum': weights[0] + 1e-12 >= cfg['reserve'],
        'estimated annual volatility <= proposed limit': vol <= cfg['risk_limit'] + 1e-12,
        'single rebalance turnover proxy <= limit': turnover <= cfg['turnover_limit'] + 1e-12,
    }
    return dict(weights=weights, gross_return=gross, net_return=net, volatility=vol,
                turnover_proxy=turnover, rules=rules, modeled_pass=all(rules.values()),
                failures=[k for k,v in rules.items() if not v],
                adoption_verdict='FAIL — governance and mandate evidence incomplete')


def run(**overrides):
    cfg = {**DEFAULTS, **overrides}
    if any(not isinstance(cfg[k], (int,float)) or not __import__('math').isfinite(cfg[k])
           for k in ('target','reserve','risk_limit','cost_bps','equity_haircut','turnover_limit')):
        raise ValueError('All numeric inputs must be finite.')
    if not (0 <= cfg['reserve'] <= 1 and 0 <= cfg['turnover_limit'] <= 1
            and 0 < cfg['risk_limit'] <= 1 and 0 <= cfg['cost_bps'] <= 1000
            and -.20 <= cfg['target'] <= .50 and 0 <= cfg['equity_haircut'] <= .50):
        raise ValueError('Input outside supported range.')
    data = p.estimate_from_csv(ROOT/'prices.csv', cfg['last_36'])
    assets = copy.deepcopy(data['assets'])
    if [a['name'] for a in assets] != TICKERS:
        raise ValueError('Expected BIL, IEF, LQD, VT in that order.')
    assets[3]['return'] -= cfg['equity_haircut']
    corr = data['correlations']
    baselines = {
        'Equal weight': evaluate([.25]*4, assets,corr,cfg),
        'Inverse volatility': evaluate(p.inverse_volatility_weights(assets),assets,corr,cfg),
        '60/40 benchmark': evaluate([0,0,.4,.6],assets,corr,cfg),
    }
    best = None
    for w in p.weight_grid(4):
        r = evaluate(w,assets,corr,cfg)
        if r['modeled_pass'] and (best is None or r['volatility'] < best['volatility'] - 1e-12):
            best = r
    return dict(config=cfg, assets=assets, observations=data['observations'],
                first_return=data['first_return'], last_return=data['last_return'],
                baselines=baselines, constrained=best)


def signal(cutoff='2026-11-17'):
    """Frozen vintage, conservatively usable only after actual retrieval day."""
    cutoff = date.fromisoformat(cutoff)
    meta = json.loads((ROOT/'data/cpi-provenance.json').read_text())
    path = ROOT/'data/cpi-vintage.csv'
    if hashlib.sha256(path.read_bytes()).hexdigest() != meta['sha256']:
        raise ValueError('CPI snapshot hash mismatch.')
    if cutoff < date.fromisoformat(meta['usable_from']):
        return dict(status='QUARANTINE', reason='Snapshot not yet retrieved at requested decision date.')
    with path.open(newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        vintage = date.fromisoformat(header[1][-8:-4]+'-'+header[1][-4:-2]+'-'+header[1][-2:])
        if vintage > cutoff:
            return dict(status='QUARANTINE', reason='Vintage is later than decision date.')
        vals = {r[0]:float(r[1]) for r in reader if len(r)==2 and r[1].strip() and date.fromisoformat(r[0]) <= cutoff}
    latest = max(vals)
    year_ago = str(int(latest[:4])-1)+latest[4:]
    if year_ago not in vals:
        return dict(status='QUARANTINE', reason='Missing matching year-ago observation.')
    yoy = vals[latest]/vals[year_ago]-1
    age = (cutoff-date.fromisoformat(latest)).days
    return dict(status='MONITOR ONLY' if age <= 90 else 'STALE — STOP',
                observation=latest, index=vals[latest], year_ago_index=vals[year_ago],
                yoy=yoy, age_days=age, reference_hurdle=yoy+.03,
                reason='No alpha claim; observed inflation does not replace the 2.5% forward assumption.')


def report():
    base = run()
    cases = {'base':{}, 'VT estimate minus 1 percentage point':{'equity_haircut':.01},
             'last 36 returns':{'last_36':True}, 'cost 100 bps':{'cost_bps':100},
             'reserve 80%':{'reserve':.8}, 'volatility cap 4%':{'risk_limit':.04},
             'combined adverse':{'equity_haircut':.01,'cost_bps':100,'reserve':.8}}
    results = {}
    for label, params in cases.items():
        item = run(**params)
        chosen = item['constrained']
        delta = (max(abs(a-b) for a,b in zip(chosen['weights'],base['constrained']['weights']))
                 if chosen and base['constrained'] else None)
        results[label] = dict(portfolio=chosen, largest_weight_change=delta,
                             stop=chosen is None or (delta is not None and delta > .10+1e-12))
    return dict(as_of='2026-11-17', price_download_claim='2026-11-01, inherited Lab 15',
                price_sha256=hashlib.sha256((ROOT/'prices.csv').read_bytes()).hexdigest(),
                base=base, signal=signal(), stresses=results,
                recommendation='REJECT production adoption; permit paper research only, 0% live allocation',
                stop=any(r['stop'] for r in results.values()))


if __name__ == '__main__':
    out = report()
    (ROOT/'visible_output.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))
