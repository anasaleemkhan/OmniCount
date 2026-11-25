@echo off
cd /d "%~dp0"
setlocal enabledelayedexpansion

echo ======================================================================
echo           👁️ OMNICOUNT PRO - SPATIAL VISION & TELEMETRY
echo ======================================================================
echo  1. Launch Modern Interactive Webpage (Browser Dashboard)
echo  2. Launch Streamlit Full Vision Dashboard
echo  3. Run Terminal CLI Inference on sample_test.jpg
echo  4. Exit
echo ======================================================================
set /p opt="Enter choice [1-4] (default: 1): "
if "%opt%"=="" set opt=1

if "%opt%"=="1" (
    echo [*] Opening Webpage in default browser...
    start "" index.html
    echo [*] Starting local Python web server at http://localhost:8000 ...
    if exist ".venv\Scripts\python.exe" (
        ".venv\Scripts\python.exe" web_server.py
    ) else (
        python web_server.py
    )
) else if "%opt%"=="2" (
    echo [*] Starting Streamlit Dashboard...
    if exist ".venv\Scripts\streamlit.exe" (
        ".venv\Scripts\streamlit.exe" run app.py
    ) else (
        streamlit run app.py
    )
) else if "%opt%"=="3" (
    echo [*] Running CLI inference...
    if exist ".venv\Scripts\python.exe" (
        ".venv\Scripts\python.exe" main.py --image sample_test.jpg
    ) else (
        python main.py --image sample_test.jpg
    )
    pause
) else (
    exit /b
)
