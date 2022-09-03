@echo off
echo.
set cwd=%~dp0
cd /d %cwd%
set arg=%*
py rgenz-file.py "%arg%"
echo.
pause