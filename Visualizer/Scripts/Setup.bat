@echo off

cd ..

virtualenv --python=C:\Users\Nikko\AppData\Local\Programs\Python\Python35\python.exe venv
call .\venv\Scripts\activate.bat

pip install -r requirements.txt