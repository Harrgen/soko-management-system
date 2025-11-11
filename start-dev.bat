@echo off
echo Starting Soko Management System...
cd /d C:\Users\ADMIN\desktop\soko-management-system
call venv\Scripts\activate
cd src
echo.
echo Virtual environment activated!
echo Starting FastAPI server...
echo.
echo Open http://localhost:8000/docs in your browser
echo Press Ctrl+C to stop the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause
