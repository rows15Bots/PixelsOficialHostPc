@echo off
setlocal enabledelayedexpansion

set PORT=5040
:start
:: Get PID using port 5040
for /f "tokens=5" %%a in ('netstat -ano ^| find "0.0.0.0:%PORT%"') do (
    set PID=%%a
)
echo %PID%
pause
:: Check if PID is found
if defined PID (
    echo Found PID: %PID%
    taskkill /F /PID %PID%
    echo Process terminated.
) else (
    echo No process found using port %PORT%.
)
pause
goto :start