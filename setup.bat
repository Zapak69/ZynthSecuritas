@echo off
set "success=[[92m+[0m]"
set "warning=[[91m![0m]"
set "info=[[36mi[0m]"
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit
)
python --version >nul
if NOT "%errorlevel%" == "0" goto py
pip install discord
pip install os
pip install subprocess
pip install pyautogui
cls
echo.
echo %success% Requirements are installed!
timeout /t 2 /nobreak >nul
if NOT exist "%~dp0\security.bat" (
    cls
    echo.
    echo %warning% security.bat not found!
    pause >nul
    exit
)
if NOT exist "%~dp0\bot_setup.bat" (
    cls
    echo.
    echo %warning% bot_setup.bat not found!
    pause >nul
    exit
)
if NOT exist "%~dp0\set_pass.bat" (
    cls
    echo.
    echo %warning% set_pass.bat not found!
    pause >nul
    exit
)
if NOT exist "%~dp0\security.pyw" (
    cls
    echo.
    echo %warning% security.pyw not found!
    pause >nul
    exit
)
copy %~dp0\security.bat "C:\"
copy %~dp0\security.pyw "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup"
start %~dp0\bot_setup.bat
start %~dp0\set_pass.bat
exit
:py
echo.
echo Python not installed or added to PATH!
echo.
echo Please install or add python to PATH to continue.
pause >nul
exit