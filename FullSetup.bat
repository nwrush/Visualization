@echo off

Set ROOT=%CD%

Set AppPath=Application
Set VisPath=Visualizer

Set PythonPath="C:\Users\rushni\AppData\Local\Programs\Python\Python35\python.exe"

REM This script should be executed from where you want to root the application

git submodule init
git submodule update

mkdir "%AppPath%"

REM Install the visualizer
xcopy "%VisPath%\*.py" "%AppPath%\"
xcopy "%VisPath%\frames\*.py" "%AppPath%\frames\"
xcopy "%VisPath%\widgets\*.py" "%AppPath%\widgets\"
xcopy "%VisPath%\requirements.txt" "%AppPath%\requirements.txt"

cd %AppPath%

virtualenv --python=%PythonPath% venv
call .\venv\Scripts\activate.bat
pip install -r requirements.txt
call .\venv\Scripts\deactivate.bat

cd %ROOT%

REM Install the preprocessor
mkdir "%AppPath%\idea_relations"

xcopy "idea_relations\*.py" "%AppPath%\idea_relations\"
xcopy "idea_relations\templates" "%AppPath%\idea_relations\templates\"
xcopy "idea_relations\*.bat" "%AppPath%\idea_relations\"
xcopy "idea_relations\*.sh" "%AppPath%\idea_relations\"
xcopy "idea_relations\*.whl" "%AppPath%\idea_relations\"
xcopy "idea_relations\requirements.txt" "%AppPath%\idea_relations\requirements.txt"

cd %AppPath%\idea_relations

virtualenv --python=%PythonPath% preprocessor_venv
call .\preprocessor_venv\Scripts\activate.bat

pip install "numpy-1.13.1+mkl-cp35-cp35m-win_amd64.whl"
pip install "scipy-0.19.1-cp35-cp35m-win_amd64.whl"
pip install -r requirements.txt

call .\preprocessor_venv\Scripts\deactivate.bat

cd %AppPath%
call .\venv\Scripts\activate.bat
