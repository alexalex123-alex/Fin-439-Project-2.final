OpenAI Codex assisted code, calculations, testing and written drafts. Alex confirmed on November 23, 2026 that the final decision is his own.

Education, not investment advice.

# Project 2 — Northbridge Investment Management

Interactive Python web app with two transparent baselines, a constrained portfolio, explicit failed rules, a dated CPI monitor and stress tests. Proposed decision: **reject production adoption; 0% live allocation, paper research only.**

## Run from a clean download

Install Python 3.11 or newer. Extract the entire repository, open a terminal in its folder, and run:

```powershell
python webapp.py
```

On Windows with the Python launcher, `py webapp.py` also works. On macOS/Linux use `python3 webapp.py`. Open [the local app](http://127.0.0.1:8502) in a browser. Stop with Ctrl+C. The server binds only to your own computer. If port 8502 is occupied, close the prior copy before restarting. **No packages, API keys, network downloads or account are needed for Project 2.** `requirements-project2.txt` documents that boundary; older Streamlit apps have separate dependencies.

Edit inputs and press Recalculate. Read pass/fail reasons for equal weight, inverse volatility, benchmark and constrained allocation. Change the window to 36 returns; the fixed default-policy stress table below remains labeled separately. The date control gates the frozen CPI snapshot; earlier-than-retrieval dates are quarantined. All full-adoption verdicts remain FAIL while mandate evidence is incomplete.

## Reproduce and validate

```powershell
python project2.py
python -m unittest discover -s tests -v
```

The first command rewrites `visible_output.json`. Read it without executing code for material inputs, dates, portfolios, breached rules, signal and stresses. The second runs eight meaningful numerical, policy, timing and web-output checks. Both must be run from the repository folder.

## Read and finish

- `docs/decision-memo.md`: recommendation, allocation range, evidence and reversal triggers.
- `docs/validation-and-ai-use.md`: verification, data boundaries, limitations and AI-use record.
- `docs/data-card.md`: signal provenance, transformations, availability and permitted use.
- `docs/locked-changed-input-record.md`: **pending human AI-off prediction and pre-run GitHub commit**.
- `docs/video-scripts.md`: three timed recording drafts, not transcripts of completed videos.
- `docs/submission-manifest.md`: required links and final submission checklist.

Northbridge's original mandate is preserved in `docs/lab13-source.md`. The objective is CPI + 3% net over five years; 5.5% nominal is only a proxy. Annual volatility limit 8%, minimum-volatility selection, hypothetical starting holdings and single-rebalance turnover screen are explicit research proposals, not client approvals. Observed feasible research range is BIL 55–90%, VT 10–45%; IEF/LQD zero in these cases. No live capital is recommended.

## Historical files

Earlier labs remain for provenance. `app.py` also starts Project 2. `lab19_app.py` preserves the old Streamlit panel, which references missing `.agents` and `reports` files. No claim is made that the legacy panel can run from this repository. Earlier lab recommendations and cost assumptions are historical and are superseded by the Project 2 memo for this submission.

Course: [Project 2](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) and [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md). Dates and points must be checked in Brightspace. Attach the final memo and validation Markdown files there; provide three YouTube links with transcripts enabled and checked. No submission, recording, student ownership confirmation or locked prediction is claimed by this build.
