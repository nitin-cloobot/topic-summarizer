@echo off
echo ========================================
echo Frontend Setup Script
echo ========================================
echo.

cd frontend

echo Installing Node dependencies...
call npm install

echo.
echo ========================================
echo Frontend setup complete!
echo ========================================
echo.
echo Next step:
echo Run start-frontend.bat to start the development server
echo.
echo Press any key to exit...
pause > nul

