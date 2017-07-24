#!/bin/bash

ROOT=$(pwd)

AppPath=Application
VisPath=Visualizer

PythonPath=/opt/tools/python/3.5.1/bin/python

git submodule init
git submodule update

mkdir $AppPath
mkdir $AppPath/frames
mkdir $AppPath/widgets

cp $VisPath/*.py $AppPath
cp $VisPath/frames/*.py $AppPath/frames/
cp $VisPath/widgets/*.py $AppPath/widgets/
cp $VisPath/requirements.txt $AppPath/requirements.txt

cd $AppPath

virtualenv --python=$PythonPath venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

cd $ROOT

mkdir $AppPath/idea_relations

cp idea_relations/*.py $AppPath/idea_relations/
cp -r idea_relations/templates $AppPath/idea_relations/templates/
cp idea_relations/*.bat $AppPath/idea_relations/
cp idea_relations/*.sh $AppPath/idea_relations/
# cp idea_relations/*.whl $AppPath/idea_relations/
cp idea_relations/requirements.txt $AppPath/idea_relations/requirements.txt

cd $AppPath/idea_relations

virtualenv --python=$PythonPath preprocessor_venv
source preprocessor_venv/bin/activate
pip install -r requirements.txt
deactivate

cd $ROOT/$AppPath
source venv/bin/activate
