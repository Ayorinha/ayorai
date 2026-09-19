@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
 echo Run INSTALL_AYORAI_OCR.bat first.
 pause
 exit /b 1
)
call .venv\Scripts\activate.bat
start "AYORAI OCR" cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:8000"
python -m uvicorn api.main:app --host 127.0.0.1 --port 8000
