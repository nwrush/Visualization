@echo off

git submodule update

Set Loc=%CD%

setlocal

Set ROOT=%~dp0
echo %ROOT%
cd %ROOT%

Set AppPath=Application
Set VisPath=Visualizer

:: This script re-copies all python files to the application folder

:: Update the visualizer
xcopy /Y "%VisPath%\*.py" "%AppPath%\"
xcopy /Y "%VisPath%\frames\*.py" "%AppPath%\frames\"
xcopy /Y  "%VisPath%\widgets\*.py" "%AppPath%\widgets\"
xcopy /Y "%VisPath%\menus\*.py" "%AppPath%\menus\"
xcopy /Y "%VisPath%\Images\*.*" "%AppPath%\Images\"
xcopy /Y "%VisPath%\events\*.py" "%AppPath%\events\"
xcopy /Y "%VisPath%\ui\*.py" "%AppPath%\ui\"

:: Update the preprocessor

xcopy /Y  "idea_relations\*.py" "%AppPath%\idea_relations\"
xcopy /Y  "idea_relations\templates" "%AppPath%\idea_relations\templates\"
xcopy /Y  "idea_relations\*.bat" "%AppPath%\idea_relations\"
xcopy /Y  "idea_relations\*.sh" "%AppPath%\idea_relations\"

endlocal

cd %Loc%

set "Loc="
