@echo off
%~d0
cd %~dp0

set /p input=请输入定时运行时间（例如23:22）： 
at %input% %~dp0search.bat
at

pause