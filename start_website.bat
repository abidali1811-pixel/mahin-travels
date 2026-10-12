@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo The project virtual environment was not found.
    echo Open this project in VS Code and install the requirements first.
    pause
    exit /b 1
)

start "Mahin Travels server" /D "%~dp0" ".venv\Scripts\python.exe" manage.py runserver 127.0.0.1:8000
timeout /t 3 /nobreak >nul
start "" "http://127.0.0.1:8000/"
