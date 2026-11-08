@echo off
rem SPDX-License-Identifier: GPL-3.0-or-later
rem
rem Windows launcher for build.py. Double-click it, or drag your dumps
rem folder onto it. If you double-click it, it uses a folder named "dumps"
rem next to this file, or asks you to drag the folder into the window.
rem Kept free of ( ) blocks around paths, so folder names with brackets work.

setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
set "RC=1"

echo Looking for Python...
set "PY="
call :findpy py
if not defined PY call :findpy python
if not defined PY call :findpy python3
if not defined PY goto nopython

echo Found: %PY%
echo.
if not "%~1"=="" goto run_args
if exist "dumps\" goto run_dumps

echo Drag your dumps folder into this window, then press Enter.
echo (That's the 3ds-jpn-english folder from gm9\out on your SD card.)
echo.
set "DUMPS="
set /p "DUMPS=Folder: "
if not defined DUMPS goto nodumps
set "DUMPS=%DUMPS:"=%"
rem Clear the screen so the dragged-in path (which includes the user name)
rem isn't left in the window if someone pastes the output into an issue.
cls
echo Building from the folder you dragged in.
echo.
%PY% build.py "%DUMPS%"
set "RC=%ERRORLEVEL%"
goto done

:run_args
%PY% build.py %*
set "RC=%ERRORLEVEL%"
goto done

:run_dumps
echo Using the dumps folder next to build.bat.
echo.
%PY% build.py dumps
set "RC=%ERRORLEVEL%"
goto done

:findpy
%1 -c "import sys; sys.exit(sys.version_info < (3, 8))" >nul 2>&1
if not errorlevel 1 set "PY=%1"
exit /b 0

:nopython
echo Python 3.8 or newer wasn't found.
echo Install "Python install manager" from the Microsoft Store, open
echo Terminal, type python and press Enter once, then try again.
echo See "Install Python" in README.md.
goto end

:nodumps
echo No folder given, nothing built.
goto end

:done
echo.
if not "%RC%"=="0" goto failed
echo Opening the out folder. Copy the folders inside out\luma\titles
echo into luma\titles on your SD card (see README, step 3).
start "" "%~dp0out"
goto end

:failed
echo The build stopped. Nothing was written; read the messages above.

:end
echo.
pause
