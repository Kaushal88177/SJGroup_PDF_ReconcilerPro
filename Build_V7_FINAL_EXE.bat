@echo off
setlocal enabledelayedexpansion
echo ============================================
echo SJ Group - PDF Reconciler V7.0 FINAL BUILDER
echo Main File: PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py
echo ============================================
echo.

set PY_FILE=PDF-Ledger-Reconciler-V7-Generic-Any-Invoice-Series.py
set EXE_NAME=SJGroup_Reconciler_V7_Generic

echo [1/5] Checking Python...
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python PATH me nahi hai!
    pause
    exit /b
)

echo [2/5] Checking main file...
if exist "%PY_FILE%" (
    echo [OK] Found: %PY_FILE%
) else (
    echo [ERROR] File not found: %PY_FILE%
    dir /b *.py
    pause
    exit /b
)

if exist "%PY_FILE%.py" (
    echo [FIX] Fixing double extension...
    ren "%PY_FILE%.py" "%PY_FILE%"
)

echo [3/5] Installing libs...
pip install --upgrade pip
pip install PyMuPDF openpyxl pyinstaller

echo [4/5] Cleaning...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
rmdir /s /q __pycache__ 2>nul
del /q *.spec 2>nul

echo [5/5] Building EXE (3-5 min)...
python -m PyInstaller --onefile --windowed --name "%EXE_NAME%" --hidden-import fitz --hidden-import openpyxl --hidden-import openpyxl.styles --collect-submodules fitz --collect-submodules openpyxl --clean "%PY_FILE%" > build_log.txt 2>&1

echo.
if exist dist\%EXE_NAME%.exe (
    echo [SUCCESS] EXE BAN GAYA!
    echo Location: %cd%\dist\%EXE_NAME%.exe
    dir dist\%EXE_NAME%.exe
    explorer dist
) else (
    echo [FAILED]
    type build_log.txt
)

pause
