param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("install", "lint", "format", "test", "run")]
    [string]$Task
)

$ErrorActionPreference = "Stop"

# Root of the project (directory containing this script -> ..)
$ProjectRoot = Split-Path -Path $PSScriptRoot -Parent
Set-Location $ProjectRoot

$VenvPath = Join-Path $ProjectRoot ".venv"
$PythonExe = Join-Path $VenvPath "Scripts\python.exe"
$PipExe = Join-Path $VenvPath "Scripts\pip.exe"

function Ensure-Venv {
    if (-not (Test-Path $PythonExe)) {
        Write-Host "Virtual environment not found. Creating .venv..." -ForegroundColor Yellow
        python -m venv ".venv"
    }
}

function Ensure-DevDependencies {
    Write-Host "Installing base dependencies from requirements.txt..." -ForegroundColor Cyan
    & $PipExe install --upgrade pip
    & $PipExe install -r "requirements.txt"

    Write-Host "Installing development dependencies (pytest, black, flake8, isort, mypy)..." -ForegroundColor Cyan
    & $PipExe install pytest>=8.0.0 black>=24.0.0 flake8>=7.0.0 isort>=5.13.0 mypy>=1.10.0

    Write-Host "Installing project in editable mode..." -ForegroundColor Cyan
    & $PipExe install -e .
}

function Invoke-Install {
    Ensure-Venv
    & $PythonExe --version | Write-Host
    Ensure-DevDependencies
    Write-Host "Install step finished." -ForegroundColor Green
}

function Invoke-Lint {
    Ensure-Venv
    Write-Host "Running flake8..." -ForegroundColor Cyan
    & $PythonExe -m flake8 src tests

    Write-Host "Running black --check..." -ForegroundColor Cyan
    & $PythonExe -m black --check src tests

    Write-Host "Running isort --check-only..." -ForegroundColor Cyan
    & $PythonExe -m isort --check-only src tests

    Write-Host "Running mypy..." -ForegroundColor Cyan
    & $PythonExe -m mypy src

    Write-Host "Lint step finished." -ForegroundColor Green
}

function Invoke-Format {
    Ensure-Venv
    Write-Host "Running black (format)..." -ForegroundColor Cyan
    & $PythonExe -m black src tests

    Write-Host "Running isort (format)..." -ForegroundColor Cyan
    & $PythonExe -m isort src tests

    Write-Host "Format step finished." -ForegroundColor Green
}

function Invoke-Test {
    Ensure-Venv
    Write-Host "Running pytest..." -ForegroundColor Cyan
    & $PythonExe -m pytest -q
    Write-Host "Test step finished." -ForegroundColor Green
}

function Invoke-Run {
    Ensure-Venv
    # NOTE: {{ cookiecutter.package_name }} will be rendered by Cookiecutter
    $module = "{{ cookiecutter.package_name }}.pipelines.train"
    Write-Host "Running training pipeline: python -m $module" -ForegroundColor Cyan
    & $PythonExe -m $module
}

switch ($Task) {
    "install" { Invoke-Install }
    "lint"    { Invoke-Lint }
    "format"  { Invoke-Format }
    "test"    { Invoke-Test }
    "run"     { Invoke-Run }
    default {
        Write-Error "Unknown task: $Task"
        exit 1
    }
}
