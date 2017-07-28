#!/bin/bash

ROOT=$(pwd)

AppPath=Application
VisPath=Visualizer

PythonPath=/opt/tools/python/3.5.1/bin/python
VenvPath=./fake_venv.sh

# Check executables for existance
if [[ ! -f "$PythonPath" ]] || [[ ! -x "$PythonPath" ]]
then
    echo Couldn\'t locate python executable at $PythonPath
    exit 1
fi

if [[ ! -f "$VenvPath" ]] || [[ ! -x "$VenvPath" ]]
then
    echo Couldn\'t locate virtualenv at $VenvPath
    exit 1
fi

mkdir $AppPath
mkdir $AppPath/frames
mkdir $AppPath/widgets
mkdir $AppPath/menus
mkdir $AppPath/Images


cp $VisPath/*.py $AppPath
cp $VisPath/frames/*.py $AppPath/frames/
cp $VisPath/widgets/*.py $AppPath/widgets/
cp $VisPath/menus/*.py $AppPath/menus/
cp $VisPath/Images/*.* $AppPath/Images/

mkdir $AppPath/idea_relations

cp idea_relations/*.py $AppPath/idea_relations/
cp -r idea_relations/templates $AppPath/idea_relations/templates/
cp idea_relations/*.bat $AppPath/idea_relations/
cp idea_relations/*.sh $AppPath/idea_relations/

cd $AppPath

$VenvPath --python=$PythonPath venv
source venv/bin/activate
pip install -r FullRequirements.txt