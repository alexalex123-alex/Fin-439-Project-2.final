"""Local interactive Python web app. Standard library only."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse
from html import escape
import json
import project2 as m


def pct(v):
    return f'{v*100:.2f}%'


def table(rows):
    if not rows:
        return '<p>INFEASIBLE: STOP. No constrained portfolio passes all modeled rules.</p>'
    return '<table><tr>'+''.join('<th>'+escape(k)+'</th>' for k in rows[0])+'</tr>'+''.join(
        '<tr>'+''.join('<td>'+escape(str(v))+'</td>' for v in r.values())+'</tr>' for r in rows)+'</table>'


def row(name,r):
    return dict(Portfolio=name,**{t:pct(w) for t,w in zip(m.TICKERS,r['weights'])},
                Net=pct(r['net_return']),Volatility=pct(r['volatility']),Turnover=pct(r['turnover_proxy']),
                Verdict='PASS modeled checks' if r['modeled_pass'] else 'FAIL: '+'; '.join(r['failures']))


def page(q):
    controls=''; cfg={}
    for k,label,default,lo,hi in [('target','Net target (%)',5.5,-20,50),('reserve','Minimum BIL (%)',3,0,100),
        ('risk_limit','Proposed volatility ceiling (%)',8,.1,100),('cost_bps','Annual cost drag (bps)',25,0,1000),
        ('equity_haircut','VT return reduction (percentage points)',0,0,50),('turnover_limit','Rebalance turnover ceiling (%)',20,0,100)]:
        raw=q.get(k,[str(default)])[0]
        cfg[k]=float(raw)/(1 if k=='cost_bps' else 100)
        controls+=f'<label>{label}<input name="{k}" type="number" min="{lo}" max="{hi}" step="0.1" value="{escape(raw)}" required></label>'
    cfg['last_36']=q.get('window',['60'])[0]=='36'
    r=m.run(**cfg); report=m.report()
    rows=[row(k,v) for k,v in r['baselines'].items()]
    if r['constrained']: rows.append(row('Constrained minimum volatility',r['constrained']))
    stresses=[]
    for k,v in report['stresses'].items():
        p=v['portfolio']
        stresses.append(dict(Case=k,Allocation=' / '.join(pct(w) for w in p['weights']) if p else 'INFEASIBLE',
            Net=pct(p['net_return']) if p else '—',Change=pct(v['largest_weight_change']) if v['largest_weight_change'] is not None else '—',Gate='STOP' if v['stop'] else 'PASS'))
    cutoff=q.get('cutoff',['2026-11-17'])[0]
    body=f'''<p>OpenAI Codex assisted code, analysis, testing and writing. Alex has confirmed ownership of the final decision. Education, not investment advice.</p>
    <h1>Northbridge · Investment committee</h1><aside><b>REJECT production adoption · 0% live allocation</b><p>Paper research only. All portfolios FAIL full mandate adoption: policy approval, actual annual turnover, spending and implementation evidence remain incomplete.</p></aside>
    <h2>Mandate</h2><p>$10m scholarship fund, ten-year horizon, $75,000 quarterly distributions. CPI + 3% net over rolling five years; 5.5% nominal planning proxy. Benchmark 60% VT / 40% LQD. BIL, IEF, LQD, VT only. Long only, fully funded; no portfolio borrowing/derivatives; 90% liquid in five days; company cap 5% with diversified-fund exemptions; annual review; annual one-way turnover at most 20% without written committee approval.</p>
    <p>Research proposals: minimum estimated volatility on a 5-percentage-point grid; 8% annual volatility ceiling. BIL-only reserve proxy (3% initially). Normal-market ETF liquidity and exemptions are assumptions. Turnover below is half absolute weight change from hypothetical 70% BIL / 30% VT; it does not prove the mandate's annual trading-ledger measure.</p>
    <h2>Run allocation</h2><form>{controls}<label>Return observations<select name="window"><option value="60" {'selected' if not cfg['last_36'] else ''}>60 months</option><option value="36" {'selected' if cfg['last_36'] else ''}>36 months</option></select></label><button>Recalculate</button></form>
    <p>{r['observations']} monthly returns, {r['first_return']} to {r['last_return']}. Inherited prices through October 2026; claimed download November 1. Historical arithmetic returns are estimates, not forecasts. Costs are an assumed annual drag; fund expenses are already reflected in adjusted prices.</p>{table(rows)}{'' if r['constrained'] else table([])}
    <h2>Annual input estimates</h2>{table([dict(Ticker=a['name'],Return=pct(a['return']),Volatility=pct(a['volatility'])) for a in r['assets']])}
    <h2>Default-policy stress audit</h2><p>These fixed cases use defaults independently of your interactive run. STOP for infeasibility or any allocation shift above 10 percentage points. Order: BIL / IEF / LQD / VT.</p>{table(stresses)}
    <h2>Point-in-time inflation monitor</h2><form><label>Decision date<input type="date" name="cutoff" value="{escape(cutoff)}"></label><button>Check availability</button></form><pre>{escape(json.dumps(m.signal(cutoff),indent=2))}</pre>
    <p>ALFRED CPIAUCSL: requested October 31 vintage, returned October 23; retrieved November 17. Earlier decision dates are quarantined. Year-over-year change uses matching months in the same vintage; missing values are never filled. Monitoring only: this does not change the forward inflation assumption or assert predictive power.</p>
    <h2>Committee ask</h2><p>Reject adoption now. Permit paper research only. Reconsider after policy approval, forward-return and cost review, spending simulation and all agreed stress gates pass. Monitor reserve dollars, annual turnover ledger, monthly risk and data freshness. See executed output and memo for the observed research allocation range.</p>
    <p><a href="/output.json">Executed output</a> · <a href="/memo">Memo</a> · <a href="/validation">Validation</a> · <a href="/data-card">Data card</a></p>'''
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Northbridge Project 2</title><style>body{font:16px system-ui;background:#f3f6f8;color:#182c3c;max-width:1250px;margin:30px auto;padding:20px}h1{font-size:36px}h2{margin-top:35px}aside{background:#ffe5b8;padding:20px;border-left:6px solid #a65400}table{border-collapse:collapse;width:100%;background:white;font-size:14px}td,th{border:1px solid #ccd6df;padding:10px;text-align:left}th{background:#193e51;color:white}form{display:flex;gap:15px;flex-wrap:wrap;background:white;padding:20px}label{display:flex;flex-direction:column;gap:5px}input,select,button{font:inherit;padding:8px}button{background:#185c69;color:white;border:0}pre{white-space:pre-wrap}p{line-height:1.6}</style>'+body+'</html>'


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        u=urlparse(self.path)
        files={'/memo':'docs/decision-memo.md','/validation':'docs/validation-and-ai-use.md','/data-card':'docs/data-card.md'}
        try:
            if u.path=='/output.json': content=json.dumps(m.report(),indent=2); mime='application/json'
            elif u.path in files: content=(m.ROOT/files[u.path]).read_text(encoding='utf-8'); mime='text/plain'
            elif u.path=='/': content=page(parse_qs(u.query)); mime='text/html'
            else: self.send_error(404); return
            self.send_response(200)
        except (ValueError,OverflowError) as e:
            content='Invalid input: '+str(e); mime='text/plain'; self.send_response(400)
        data=content.encode()
        self.send_header('Content-Type',mime+'; charset=utf-8'); self.send_header('Content-Length',str(len(data)))
        self.end_headers(); self.wfile.write(data)


if __name__=='__main__':
    print('Open http://127.0.0.1:8502 ; Ctrl+C stops',flush=True)
    ThreadingHTTPServer(('127.0.0.1',8502),Handler).serve_forever()
