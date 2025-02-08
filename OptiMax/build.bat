@echo off

echo Building executable...

g++ -Os -flto -s main.cpp

echo Stripping down the executable...

strip --strip-all a.exe

ren a.exe OptiMax.exe