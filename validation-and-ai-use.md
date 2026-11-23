# Validation and AI-use record

OpenAI Codex assisted implementation, numerical analysis, testing and writing on November 17, 2026. Alex confirmed ownership of the final decision on November 23, 2026. Education, not investment advice.

## Scope and reproducibility

Run `python -m unittest discover -s tests -v` and `python project2.py` from the repository folder. Python 3.11+ and the standard library suffice. Web entry point: `python webapp.py` or `python app.py`; visit http://127.0.0.1:8502. `visible_output.json` is an actual executed output, not the course starter's example. As-of date: November 17, 2026 after CPI retrieval. Fund history ends October 2026. Source definitions, URL, timestamp and snapshot hash are in `docs/data-card.md` and `data/cpi-provenance.json`.

Eight automated checks passed on November 17:

| Check | Evidence / result |
|---|---|
| Price-return estimates | Independently recomputed monthly ratios, arithmetic means and sample standard deviations agree |
| Covariance cross terms | Hand-sized 2-asset case gives variance 0.0375 |
| Search optimum | Every feasible 5-point-grid candidate has volatility at least that of selected portfolio |
| Baseline and governance failures | Benchmark reserve breach and universal full-adoption FAIL retained |
| Stress gates | Window instability and reserve infeasibility stop; exactly 10-point cost change passes threshold |
| Invalid input | NaN, reserve above 100%, negative risk cap rejected |
| Signal timing | Pre-retrieval date quarantined; same-vintage annual rate agrees; stale future date stops |
| Rendered web content | Both baselines, reject decision and full-adoption warning appear; invalid values rejected |

Tests verify calculations and decision gates, not future profitability. The optimization test checks the discrete grid only, not a continuous optimum. Independent price reconstruction uses the same source CSV, so it does not authenticate the source data.

## Cold-start and integration record

Initial repository review found that the old Lab 19 `app.py` referred to `.agents` and `reports` files absent from Git. Resolution: preserve it as `lab19_app.py` and provide a complete standard-library Project 2 app with bundled input snapshots. The earlier Lab 19 launcher/dependency path is no longer required. A first test invocation from the parent folder failed imports; documented commands now explicitly start in the repository folder, where all eight tests pass.

The local HTTP smoke check exercises the home page, 36-month run, infeasible reserve run, JSON output, quarantine date, all three document routes and invalid-input HTTP 400. Its results are saved in `docs/http-check.txt`. This is an assistant-operated test, not a student's manual walkthrough. Update November 23: Alex reports that his partner completed a clean run in approximately three minutes and found the result. No fix was needed. See `docs/partner-cold-run-report.md`; the command and result location were subsequently confirmed; README-only/separate-machine conditions still need confirmation.

## Material assumptions and limitations

- The Northbridge mandate was recovered from Alex's Lab 13 repository and preserved verbatim in `docs/lab13-source.md`. The client risk objective was unresolved there. Minimum estimated volatility and an 8% ceiling are proposed research policy, not approved mandates.
- The 5.5% net hurdle is a planning proxy, not evidence of CPI + 3% net attainment over rolling five-year periods. Annual arithmetic mean is not compound growth. No out-of-sample backtest or spending simulation is reported.
- All-cost allowance is assumed at 25 bps annually and stressed to 100 bps. It is a deterministic return drag, not execution-cost estimation. Fund expenses are not deducted twice. Taxes, bid/ask spreads and dynamic market impact are unmodeled.
- Starting holdings are hypothetical 70% BIL / 30% VT. Half absolute weight change approximates one fully funded rebalance, not annual turnover based on purchases, sales and average month-end value. Actual holdings, ledger and value history are needed for full compliance.
- Only BIL counts toward the reserve; ETFs are assumed liquid in normal markets and exempt as diversified funds from the company cap. No look-through derivatives certification or stressed-liquidation evidence exists. Reserve dollars must be recalculated with portfolio value.
- The CPI data is a real retrieved ALFRED vintage, hash-checked and gated by retrieval date. It is a monitor; no predictive return benefit is claimed. Ninety days from its month-start observation label is a proposed freshness convention. Intraday availability is not certified.
- Price history is inherited from Lab 15 and hashed in the visible output. The earlier Yahoo retrieval claim is not independently authenticated; vendor-adjusted history can change. It is not asserted to be point-in-time price history.
- Full adoption fails for all portfolios. Proposed recommendation is reject production adoption, 0% live capital; paper research only. Baseline modeled failures are separately shown.

## AI uses and dispositions

Tool: OpenAI Codex desktop assistant, underlying model family GPT-6 as exposed in this session; exact service model identifier/build is not exposed. Interaction date November 17, 2026. Do not substitute a guessed version.

| Material AI use | Disposition and verification |
|---|---|
| Read course instructions and inspect existing repository | Accepted; requirements mapped to deliverables and missing human steps identified |
| Propose risk ceiling, cost allowance and turnover screen | Kept as labeled research assumptions; committee approval remains unresolved |
| Integrate portfolio engine and browser UI | Accepted after standard-library unit and HTTP checks |
| Download dated CPI snapshot and derive rate | Accepted with original bytes, URL, actual timestamp, hash and same-vintage formula |
| Draft memo and recommend rejecting adoption | Proposed decision supported by 25-point window instability and infeasible constraint runs; Alex must review |
| Prepare video scripts and manifest | Draft preparation only; no recording, transcript, upload, access check or submission claimed |
| Locked changed-input prediction | Not generated or claimed; reserved for human AI-off work before a new run |

One checked AI claim: an earlier gross-return allocation of 70% BIL / 30% VT was not carried forward as a net-of-cost optimum. Adding the assumed 25 bps drag moves the feasible minimum-volatility grid solution to 65% BIL / 35% VT, net estimate 5.8250%. The numerical tests and saved output support that correction. This check was performed by the assistant; Video 1 should identify a check Alex actually repeats and understands.

## Locked Changed-Input Record

**Incomplete.** See `docs/locked-changed-input-record.md` for the exact sequence and required fields. No independently authored AI-off prediction, pre-run immutable GitHub commit or subsequent result is claimed. This build's executed stresses cannot be relabeled to meet that requirement.

## Remaining submission evidence

Alex must review and own the analysis/decision, complete the locked record, record three videos within the course limits, enable and correct transcripts, publish YouTube links, verify logged-out access, freeze links in the manifest and attach the final Markdown files in Brightspace. No deadline is invented; consult the assignment header.

## Student confirmation — November 23, 2026

Alex confirmed that the final decision is his own and reported a three-minute clean partner run with the result successfully found. This is user-reported evidence, not a newly executed assistant test. Alex subsequently confirmed `python webapp.py` and the local app decision banner / Run allocation table as the command and result location.

## Reported window experiment — November 23, 2026

See `partner-cold-run-report.md`: Alex reports expecting volatility to increase when switching 60 to 36 returns. BIL 87.35% to 92.89% is the inverse-volatility baseline weight; its portfolio volatility instead decreases from 1.36% to 0.60%. The report preserves the original expectation and explains the mismatch. No pre-run immutable prediction commit has been supplied, so the locked-record requirement remains incomplete.

## LQD follow-up supplied by Alex

Alex reports looking at BIL first, then predicting increased LQD volatility and rerunning the 60-to-36-return window change before inspecting LQD. See `lqd-prediction.md` for the attributed sequence, assistant-reproduced results, distinction between weights and volatility, and missing pre-run GitHub-lock evidence. This follow-up does not certify the locked-record requirement complete.
