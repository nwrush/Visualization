@echo off

setlocal

Set ROOT=%CD%

Set AppPath=Application
Set VisPath=Visualizer

:: This script re-copies all python files to the application folder

:: Update the visualizer
xcopy /Y "%VisPath%\*.py" "%AppPath%\"
xcopy /Y "%VisPath%\frames\*.py" "%AppPath%\frames\"
xcopy /Y  "%VisPath%\widgets\*.py" "%AppPath%\widgets\"
xcopy /Y "%VisPath%\menus\*.py" "%AppPath%\menus\"
xcopy /Y "%VisPath%\Images\*.*" "%AppPath%\Images\"

:: Update the preprocessor

xcopy /Y  "idea_relations\*.py" "%AppPath%\idea_relations\"
xcopy /Y  "idea_relations\templates" "%AppPath%\idea_relations\templates\"
xcopy /Y  "idea_relations\*.bat" "%AppPath%\idea_relations\"
xcopy /Y  "idea_relations\*.sh" "%AppPath%\idea_relations\"

endlocal & Set AppPath=%AppPath%

cd %AppPath%

set "AppPath="
