#!/bin/bash

source ../venv/bin/activate

for f in *.ui
do
    filename=$(basename "$f")
    filename="${filename%.*}"
    pyuic5 -o "$filename.py" $f
done
