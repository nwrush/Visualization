@echo off

cd ..

virtualenv --python=C:\Users\rushni\AppData\Local\Programs\Python\Python35\python.exe venv
call .\venv\Scripts\activate.bat

pip install -r requirements.txt