@echo off
%~d0
cd %~dp0

for /f "tokens=*" %%a in (keywords) do (
  python search googleshopping "%%a" 10
)

pause