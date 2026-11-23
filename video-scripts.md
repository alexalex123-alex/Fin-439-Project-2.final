# Recording drafts — NOT completed videos or transcripts

Use these as prompts, then speak in your own words after reviewing the model. Replace the ownership sentence only when true. Start each video with: “I used OpenAI Codex to help build code, check calculations and draft explanations. I reviewed the analysis and the decision is mine. This is education, not investment advice.” Do not claim the review before doing it.

## Video 1: Evolution and one checked AI output — target 2:40, maximum 3:00

- **0:00–0:20:** Opening disclosures and Northbridge's scholarship objective.
- **0:20–0:55:** Explain the progression: Lab 13 mandate; Lab 15 constrained allocation and unstable estimates; Lab 17 timing audit; Project 2 combines decision checks. The Lab 19 company panel is historical research, not a justified allocation model.
- **0:55–1:40:** Open the current app and saved output. Explain the check you personally repeat: gross return for 70% BIL / 30% VT misses the unchanged 5.5% net hurdle after the assumed 25 bps drag. The revised grid finds 65% / 35%, net 5.83%. Recompute a weighted mean minus costs using the shown inputs before recording.
- **1:40–2:15:** Explain why the 36-return case moves 25 points and stops adoption; precise code does not remove estimation uncertainty.
- **2:15–2:40:** State your reviewed reject/paper-only decision and what could reverse it. Discuss the new locked experiment only after completing it; do not invent personal results.

## Video 2: Code walkthrough — target 4:25, maximum 5:00

- **0:00–0:20:** Opening disclosures.
- **0:20–0:55:** README cold start; `python webapp.py`, standard library only, bundled data.
- **0:55–1:40:** `portfolio.py`: monthly ratios; arithmetic annualization; covariance includes both cross terms; final 36 returns require 37 prices.
- **1:40–2:35:** `project2.py`: `evaluate`, `run`; cost drag; reserve, volatility and hypothetical rebalance checks; enumerate all 1,771 grid mixes; no feasible mix returns None.
- **2:35–3:15:** `signal`: inspect provenance JSON, hash, actual-retrieval gate, dated column, missing match handling and same-vintage annual rate. Explain why a date label is not a release time.
- **3:15–4:00:** `webapp.py` request handling and forms; live default versus independently labeled fixed stress audit; render invalid input safely.
- **4:00–4:25:** Run `python -m unittest discover -s tests -v`; explain what tests verify and what they cannot establish.

## Video 3: Investment committee — target 4:30, maximum 5:00

**Have the app running live on screen from the opening frame.**

- **0:00–0:25:** Opening disclosures over the running app; ask committee to reject live adoption and allow paper research, 0% live allocation.
- **0:25–1:10:** Mandate: $10m, quarterly $75,000, CPI + 3% over rolling five years, 3% initial reserve, benchmark and universe. Distinguish proposed volatility cap from client-approved policy.
- **1:10–1:55:** Show the two baselines, benchmark and selected portfolio. Explain failed rules and universal full-adoption failure. The selected portfolio passes modeled screens, not the full client mandate.
- **1:55–2:40:** Change window to 36 returns; show allocation change. Show fixed stress table and infeasible reserve case. Explain the above-10-point stop rule.
- **2:40–3:20:** Show CPI monitor and card. Snapshot gate, 3.7173% annual rate, 6.7173% monitoring reference; no backtest or mechanical signal allocation.
- **3:20–4:00:** Observed research envelope BIL 55–90%, VT 10–45%; no live approval. Real trading ledger, cost review, risk approval and scholarship simulation remain necessary.
- **4:00–4:30:** Monitoring and reversal triggers; summarize YOUR completed locked experiment only after it exists, otherwise disclose it is pending. Close with committee ask.

## After recording

Upload as public or unlisted YouTube videos, enable transcripts/captions, check tickers, percentages, attribution and financial terms, then export actual transcripts as `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, `docs/transcript-video-3.txt`. Do not rename these scripts as transcripts. Add exact durations, final timestamp indices and actual YouTube URLs to the manifest; test access logged out.
