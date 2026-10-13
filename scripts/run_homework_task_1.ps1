$ProjectRoot = Split-Path $PSScriptRoot -Parent

$env:PYTHONPATH = "$ProjectRoot\src"

& "$ProjectRoot\.venv\Scripts\python.exe" "$ProjectRoot\src\core\tasks\homework1\task1.py"