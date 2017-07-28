@echo off

setlocal

IF "%1"=="" (
    Set WheelPath=.
) ELSE (
    Set WheelPath=%1
)

pscp -P 1255 nikko@zin.cs.washington.edu:/home/nikko/storage/*.whl %WheelPath%