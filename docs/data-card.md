# CPI point-in-time data card

| Field | Record |
|---|---|
| Producer / distributor | U.S. Bureau of Labor Statistics / Federal Reserve Bank of St. Louis, ALFRED |
| Series | CPIAUCSL, all-items urban consumer price index, seasonally adjusted |
| Native units / frequency | Index, 1982–1984 = 100; monthly |
| Source | https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-10-31 |
| Snapshot | `data/cpi-vintage.csv`; retrieval timestamp, URL and SHA-256 in `data/cpi-provenance.json` |
| Requested / returned vintage | October 31 / October 23, 2026; returned column `CPIAUCSL_20261023` |
| Decision boundary | November 17, 2026, after actual retrieval. Date-only app is an end-of-day research tool. No intraday or historical release-time certification is claimed. |
| Signal | `(latest index / same month one year earlier - 1)`, same snapshot for numerator and denominator |
| Observed signal | September 2026: 336.298 / September 2025: 324.245 − 1 = 3.7173% year over year |
| Permitted use | Inflation monitoring; observed CPI + 3% reference is 6.7173%, distinct from the forward 5.5% proxy. No allocation override or alpha claim. |
| Publication timing | Observation date labels a month, not its release. The snapshot is quarantined before its actual retrieval date. |
| Revisions | Seasonal adjustment can revise history. A dated vintage preserves a different information set from today's history. |
| Missing data | Blanks stay missing, including October 2025. No zero replacement, interpolation or synthetic year-ago match. |
| Freshness | Proposed monitor rule: STOP after 90 calendar days from latest observation's month-start label. Age on November 17 is 77 days. This is a research convention, not a verified release schedule. |
| Controls | Hash verification, no future vintage, no observations after cutoff, matched year-ago observation, pre-retrieval quarantine |
| Limitations | One frozen vintage is not a historical vintage panel or a backtest. The client has not approved seasonally adjusted versus unadjusted CPI for actual performance evaluation. |

Metadata: [FRED](https://fred.stlouisfed.org/series/CPIAUCSL), [ALFRED help](https://alfred.stlouisfed.org/help), [BLS seasonal adjustment](https://www.bls.gov/cpi/seasonal-adjustment/).

## Portfolio-price data

`prices.csv` is inherited unchanged from Lab 15: 61 shared month-end adjusted prices, October 2021–October 2026, for BIL/IEF/LQD/VT. Lab 15 reports Yahoo downloads on November 1, 2026 and links each source URL. The original raw daily downloads and retrieval receipts are absent; the claimed historical retrieval date has not been independently authenticated. Hashing the current file certifies this build's bytes, not that earlier claim. Do not present these adjusted prices as historically unrevised point-in-time prices.

The engine computes 60 monthly returns or the final 36 returns, arithmetic mean × 12, sample standard deviation × √12, and matching-window sample correlations. Monthly adjusted prices approximate distributions and fund expenses; they do not model actual trade execution. No annual performance backtest, spending simulation, out-of-sample success or five-year real-return attainment is asserted.
