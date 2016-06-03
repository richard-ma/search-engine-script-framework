@echo off

for /f "tokens=*" %%a in (keywords) do (
  python search googleshopping "%%a" 10
)

pause