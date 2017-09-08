#!/bin/bash

git submodule update

ROOT=$(pwd)

AppPath=Application
VisPath=Visualizer

# Update Visualizer
cp -u $VisPath/*.py $AppPath
cp -u $VisPath/frames/*.py $AppPath/frames/
cp -u $VisPath/widgets/*.py $AppPath/widgets/
cp -u $VisPath/menus/*.py $AppPath/menus/
cp -u $VisPath/Images/*.* $AppPath/Images/
cp -u $VisPath/events/*.py $AppPath/events/
cp -u $VisPath/ui/*.py $AppPath/ui
cp -u $VisPath/models/*.py $AppPath/models

# Update Idea Relations
cp -u idea_relations/*.py $AppPath/idea_relations/
cp -u -r idea_relations/templates $AppPath/idea_relations/templates/
cp -u idea_relations/*.bat $AppPath/idea_relations/
cp -u idea_relations/*.sh $AppPath/idea_relations/
