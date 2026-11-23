> Historical record of the earlier local build. The current submission repository is https://github.com/alexalex123-alex/Fin-439-Project-2.final. Use the corrected Project2-GitHub-Ready folder for the current upload; the older bundle workflow below concerns the earlier repository.

# Local commit and GitHub publication status

The report and app were committed locally on branch `project2-readiness`. The build/report commit is `617e148af52521d6ba765fac71daf663b00b8c2d`. It was authored as Codex assistant, not as an independent student prediction. A subsequent packaging commit preserves this status and snapshot byte handling.

GitHub push was attempted but failed because usable authentication was unavailable. These commits have NOT been published to GitHub. The LQD account is retrospective, not a pre-run prediction lock.

The upload ZIP includes `Project2-commits.bundle`, which preserves the local Git history. After extracting the ZIP, open a terminal in the folder containing the bundle and run:

```powershell
git clone -b project2-readiness Project2-commits.bundle Project2-with-history
cd Project2-with-history
git remote set-url origin https://github.com/alexalex123-alex/FIN-439.pt2.git
git push -u origin project2-readiness
```

Authenticate using your own GitHub account when prompted. These commands publish a separate branch; they do not replace main. After pushing, inspect the branch on GitHub and merge it through a pull request if you want it on main. Then update the submission manifest to the actual published final commit. No credentials are included in the bundle or ZIP.

If Git is unavailable, the `Project2` folder can instead be uploaded through GitHub; that route uploads the files but does not retain the enclosed local commit history automatically.
