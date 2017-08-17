@echo off

if not exist "..\processed_data" mkdir ..\processed_data

pscp -P 1255 nikko@zin.cs.washington.edu:/home/nikko/visualization/Visualization/idea_relations/*.p ..\processed_data\.