@echo off

setlocal

Set ROOT=%CD%

Set AppPath=Application
Set VisPath=Visualizer

Set PythonPath="C:\Users\rushni\AppData\Local\Programs\Python\Python35\python.exe"

:: This script should be executed from where you want to root the application

REM git submodule init
REM git submodule update

mkdir "%AppPath%"

:: Install the visualizer
xcopy "%VisPath%\*.py" "%AppPath%\"
xcopy "%VisPath%\frames\*.py" "%AppPath%\frames\"
xcopy "%VisPath%\widgets\*.py" "%AppPath%\widgets\"
xcopy "%VisPath%\menus\*.py" "%AppPath%\menus\"
xcopy "%VisPath%\Images\*.*" "%AppPath%\Images\"

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
