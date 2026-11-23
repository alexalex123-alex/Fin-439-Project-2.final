import math
import unittest
import project2 as m
import portfolio as p
import webapp


class ProjectTests(unittest.TestCase):
    def test_estimates_match_independent_monthly_calculation(self):
        import csv, statistics
        with (m.ROOT/'prices.csv').open() as f:
            rows=list(csv.reader(f))[1:]
        prices=[[float(x) for x in r[1:]] for r in rows]
        got=m.run()
        for i,a in enumerate(got['assets']):
            returns=[b[i]/a[i]-1 for a,b in zip(prices,prices[1:])]
            self.assertAlmostEqual(a['return'],sum(returns)/len(returns)*12)
            self.assertAlmostEqual(a['volatility'],statistics.stdev(returns)*math.sqrt(12))

    def test_cross_asset_variance(self):
        w=[.5,.5]
        self.assertAlmostEqual(p.portfolio_volatility(w,[[.04,.01],[.01,.09]]),math.sqrt(.0375))

    def test_all_feasible_candidates_rank_above_selected(self):
        r=m.run(); best=r['constrained']
        self.assertTrue(best['modeled_pass'])
        d=p.estimate_from_csv(m.ROOT/'prices.csv')
        for w in p.weight_grid(4):
            test=m.evaluate(w,r['assets'],d['correlations'],r['config'])
            if test['modeled_pass']: self.assertGreaterEqual(test['volatility']+1e-12,best['volatility'])

    def test_baseline_failures_and_full_adoption_gate(self):
        r=m.run()
        self.assertIn('BIL reserve >= minimum',r['baselines']['60/40 benchmark']['failures'])
        for v in r['baselines'].values(): self.assertTrue(v['adoption_verdict'].startswith('FAIL'))
        self.assertTrue(r['constrained']['adoption_verdict'].startswith('FAIL'))

    def test_stress_stop_and_infeasibility(self):
        r=m.report()
        self.assertTrue(r['stop'])
        self.assertTrue(r['stresses']['last 36 returns']['stop'])
        self.assertIsNone(r['stresses']['reserve 80%']['portfolio'])
        self.assertFalse(r['stresses']['cost 100 bps']['stop'])

    def test_invalid_inputs_fail_closed(self):
        for kw in [dict(cost_bps=float('nan')),dict(reserve=1.1),dict(risk_limit=-1)]:
            with self.assertRaises(ValueError): m.run(**kw)

    def test_asof_quarantine_and_stale_signal(self):
        self.assertEqual(m.signal('2026-11-16')['status'],'QUARANTINE')
        s=m.signal()
        self.assertEqual(s['status'],'MONITOR ONLY')
        self.assertEqual(m.signal('2027-01-01')['status'],'STALE — STOP')
        self.assertAlmostEqual(s['yoy'],336.298/324.245-1)

    def test_web_output_and_input_validation(self):
        html=webapp.page({})
        self.assertIn('Equal weight',html)
        self.assertIn('Inverse volatility',html)
        self.assertIn('REJECT production adoption',html)
        self.assertIn('FAIL full mandate',html)
        with self.assertRaises(ValueError): webapp.page({'cost_bps':['nan']})


if __name__=='__main__': unittest.main()
