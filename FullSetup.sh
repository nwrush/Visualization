#!/bin/bash

PythonPath="$(which python3)"
VenvPath="$(which virtualenv)" # Ideally the same one provided by the python installation you pointed to above

git submodule init
git submodule update

ROOT=$(pwd)

AppPath=Application
VisPath=Visualizer

# Check executables for existance
if [[ ! -f "$PythonPath" ]] || [[ ! -x "$PythonPath" ]]
then
    echo Couldn\'t locate python executable at $PythonPath
    exit 1
else
    echo Using python executable at $PythonPath
fi

if [[ ! -f "$VenvPath" ]] || [[ ! -x "$VenvPath" ]]
then
    echo Couldn\'t locate virtualenv at $VenvPath
    exit 1
else
    echo Using virtualenv at $VenvPath
fi

mkdir $AppPath
mkdir $AppPath/frames
mkdir $AppPath/widgets
mkdir $AppPath/menus
mkdir $AppPath/events
mkdir $AppPath/ui
mkdir $AppPath/models


cp $VisPath/*.py $AppPath
cp $VisPath/frames/*.py $AppPath/frames/
cp $VisPath/widgets/*.py $AppPath/widgets/
cp $VisPath/menus/*.py $AppPath/menus/
cp $VisPath/events/*.py $AppPath/events/
cp $VisPath/ui/*.py $AppPath/ui
cp $VisPath/models/*.py $AppPath/models

mkdir $AppPath/idea_relations

cp idea_relations/*.py $AppPath/idea_relations/
cp -r idea_relations/templates $AppPath/idea_relations/templates/
cp idea_relations/*.bat $AppPath/idea_relations/
cp idea_relations/*.sh $AppPath/idea_relations/

cp FullRequirements.txt $AppPath/FullRequirements.txt

cd $AppPath

$VenvPath --python=$PythonPath venv
source venv/bin/activate
pip install --upgrade pip

pip install -r FullRequirements.txt
