@echo off

call ..\venv\Scripts\activate.bat

for %%f in (*.ui) do (

    pyuic5 -o "%%~nf.py" "%%~nf.ui"
)
