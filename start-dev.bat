@echo off
REM ==============================================
REM Start-dev script for Soko Management System
REM ==============================================

echo Starting Soko Management System...

REM Navigate to project directory
cd /d C:\Users\ADMIN\desktop\soko-management-system

REM Activate virtual environment
call venv\Scripts\activate
if errorlevel 1 (
    echo Failed to activate virtual environment!
    pause
    exit /b 1
)

echo.
echo Virtual environment activated!

REM Navigate to src folder
cd src

echo.
echo Starting FastAPI server...
echo Open http://localhost:8000/docs in your browser
echo Press Ctrl+C to stop the server
echo.

REM Start FastAPI with live reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

echo.
echo Server stopped.
pause
