@echo off

setlocal

Set PythonPath="C:\Users\rushni\AppData\Local\Programs\Python\Python35\python.exe"

git submodule init
git submodule update

Set ROOT=%CD%

Set AppPath=Application
Set VisPath=Visualizer

IF NOT EXIST %PythonPath% (
    ECHO Python executable at %PythonPath% was not found
    EXIT /B 1
)

:: This script should be executed from where you want to root the application

mkdir "%AppPath%"

:: Install the visualizer
xcopy "%VisPath%\*.py" "%AppPath%\"
xcopy "%VisPath%\frames\*.py" "%AppPath%\frames\"
xcopy "%VisPath%\widgets\*.py" "%AppPath%\widgets\"
xcopy "%VisPath%\menus\*.py" "%AppPath%\menus\"
xcopy "%VisPath%\Images\*.*" "%AppPath%\Images\"
xcopy "%VisPath%\events\*.py" "%AppPath%\events\"
xcopy "%VisPath%\ui\*.py" "%AppPath%\ui\"

:: Install the preprocessor
mkdir "%AppPath%\idea_relations"

xcopy "idea_relations\*.py" "%AppPath%\idea_relations\"
xcopy "idea_relations\templates" "%AppPath%\idea_relations\templates\"
xcopy "idea_relations\*.bat" "%AppPath%\idea_relations\"
xcopy "idea_relations\*.sh" "%AppPath%\idea_relations\"


:: Install the virtual environment
copy FullRequirements.txt %AppPath%\FullRequirements.txt
call GetWheels.bat %AppPath%

endlocal & Set AppPath=%AppPath% & Set PythonPath=%PythonPath%
cd %AppPath%

virtualenv --python=%PythonPath% venv
call .\venv\Scripts\activate.bat

pip install "numpy-1.13.1+mkl-cp35-cp35m-win_amd64.whl"
pip install "scipy-0.19.1-cp35-cp35m-win_amd64.whl"
pip install -r FullRequirements.txt

Set "AppPath="
Set "PythonPath="
