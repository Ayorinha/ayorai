@echo off
setlocal
cd /d "%~dp0"
echo ============================================
echo AYORAI OFFLINE OCR - INSTALLER
echo ============================================
where py >nul 2>&1
if %errorlevel% neq 0 (
  where python >nul 2>&1
  if %errorlevel% neq 0 (
    echo Python not found. Trying winget...
    winget install --id Python.Python.3.12 -e --scope user
    if %errorlevel% neq 0 (
      echo Install Python 3.11+ and run this file again.
      pause
      exit /b 1
    )
  )
)
if not exist .venv py -3 -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r api\requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\extract_oneocr.ps1"
if %errorlevel% neq 0 (
  echo OneOCR runtime extraction failed.
  pause
  exit /b 1
)
echo Installation completed. Run START_AYORAI_OCR.bat
pause
