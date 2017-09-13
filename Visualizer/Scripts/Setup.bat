@echo off

cd ..

virtualenv --python=C:\Python36\python.exe venv
call .\venv\Scripts\activate.bat

pip install -r requirements.txt