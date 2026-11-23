$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$projectPython = Join-Path $PSScriptRoot '.venv/Scripts/python.exe'
$bundledPython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
if (Test-Path -LiteralPath $projectPython) {
    & $projectPython webapp.py
} elseif (Test-Path -LiteralPath $bundledPython) {
    & $bundledPython webapp.py
} else {
    & python webapp.py
}
