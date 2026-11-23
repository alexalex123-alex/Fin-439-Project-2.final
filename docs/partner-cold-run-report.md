# Project 2 — Partner cold-run report

## Purpose

Check whether another person could start the Project 2 application and find its result.

## Reported result

My partner completed a clean run in approximately **3 minutes** and successfully found the result. No failure was reported, so no fix or corrective rerun was needed.

| Required detail | Record |
|---|---|
| Elapsed time | Approximately 3 minutes |
| First failure | None reported; clean run |
| Result found | Yes, confirmed by my partner |
| Fix required | None |
| Exact command used | `python webapp.py` (confirmed by Alex) |
| Exact result location | http://127.0.0.1:8502 — top decision banner and portfolio table under Run allocation (confirmed by Alex) |

This report records the partner outcome Alex reported on November 23, 2026; the actual test date and partner identity were not supplied. It does not independently verify that the partner used only the README or a separate machine. Confirm those details rather than assuming them.

## Final decision ownership

I confirm that the final decision is mine: **reject production adoption, allocate 0% of live capital to this process, and permit paper research only**. Reconsider adoption after policy approval, forward-return and cost review, spending validation, and successful completion of the agreed stress gates.

OpenAI Codex assisted the application, calculations and report wording. The partner-run outcome and decision-ownership confirmation were supplied by Alex. Education, not investment advice.

## Changed-window experiment — reported after the run

I changed the return-observation window from **60 months to 36 months**. I report that, before trying it, I expected volatility to increase. The displayed BIL figure increased from **87.35% to 92.89%**, or **5.54 percentage points** using the displayed rounded values.

On checking the table labels, these figures are **BIL allocation weights in the inverse-volatility baseline**, not volatility measurements. Recomputing the two windows with the bundled data confirms the weights. The inverse-volatility portfolio's estimated annual volatility actually **decreases from 1.36% to 0.60%**. Thus, the observed increase in BIL weight does not confirm my prediction of increased volatility; the measured portfolio volatility moves in the opposite direction. More weight in the cash-proxy fund is consistent with a more defensive baseline mix, although changing the window also changes asset risk and correlation estimates.

Both windows fail the baseline's modeled net-return and hypothetical rebalance-turnover screens, and full-adoption status remains FAIL. My final decision remains **reject production adoption; 0% live allocation; paper research only**.

This account and prediction were supplied to the assistant after the run. No pre-run prediction commit, push timestamp or immutable GitHub URL has been supplied. This experiment is documented as completed exploratory work, **not a completed Locked Changed-Input Record**. The 60-to-36 window comparison was already included in the AI-assisted project stresses. A new independently predicted change, committed and pushed before execution, is still needed for that requirement. Other controls and the actual run time were not independently captured; assistant verification above holds other settings at their defaults.

## LQD follow-up supplied by Alex

Alex reports looking at BIL first, then predicting increased LQD volatility and rerunning the 60-to-36-return window change before inspecting LQD. See `lqd-prediction.md` for the attributed sequence, assistant-reproduced results, distinction between weights and volatility, and missing pre-run GitHub-lock evidence. This follow-up does not certify the locked-record requirement complete.
