# LQD prediction and rerun — retrospective record

## Student-reported sequence

Alex reports that he first examined BIL's result when reducing the return-observation window from **60 to 36 monthly returns**. He then predicted an **increase in volatility for LQD**, before inspecting its result, and reran the window change. This sequence is based on Alex's report in this chat; no original run timestamp, screenshot or pre-run GitHub commit was supplied. Other controls used in his rerun were not independently captured.

The expectation above was supplied by Alex. AI-off conditions were not independently established. No reason for the predicted direction or expected decision effect was supplied; these are not invented here.

## Assistant reproduction and interpretation

An assistant reproduction holds all other inputs at the documented defaults and compares the bundled data's 60-return and final-36-return windows. These reproduced outputs are saved in `docs/lqd-rerun-output.json`; they are not represented as screenshots or original outputs from Alex's run.

- **60 monthly returns**: LQD's own annualized return volatility **9.85%**; LQD weight in the inverse-volatility baseline **4.32%**; total inverse-volatility portfolio volatility **1.36%**.
- **36 monthly returns**: LQD's own annualized return volatility **7.73%**; LQD weight in the inverse-volatility baseline **2.52%**; total inverse-volatility portfolio volatility **0.60%**.

LQD's estimated volatility decreases, so this reproduction does **not** support the prediction of increased volatility. Allocation weights and volatility are distinct measures. A shorter sample changes the estimated return variation and correlations; fewer observations do not mechanically imply higher measured volatility. This comparison does not identify the precise market cause of the decrease.

The inverse-volatility baseline fails the modeled return and hypothetical rebalance-turnover screens in both windows. Full production adoption remains rejected. The changed window also triggers the existing constrained-portfolio stability stop. Alex has confirmed ownership of the final decision: **reject production adoption, 0% live allocation, paper research only**.

## Commit and requirement status

This document is being committed after the reported rerun. A current commit preserves the account from now onward; it does not establish a prediction pushed before execution. The app already calculated all four funds in its earlier window stress, even though Alex reports initially examining only BIL. Both facts are retained.

The course's pre-run GitHub-lock requirement is therefore **not certified complete**. Instructor acceptance of this retrospective sequence must not be assumed. No backdating, pre-run timestamp or prior push is claimed. A newly executed experiment preceded by a genuine human AI-off prediction and GitHub push remains the straightforward way to satisfy that requirement.

OpenAI Codex assisted documentation and reproduced the calculations. Student-reported sequence and prediction are attributed to Alex. Education, not investment advice.
