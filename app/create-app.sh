#!/bin/bash

py2applet-3.8 --make-setup $1.py $1.icns click.mp3 win.mp3
python setup.py py2app

echo rm -rf /Applications/$1.app 
rm -rf /Applications/$1.app 

echo cp -r dist/$1.app /Applications/
cp -r dist/$1.app /Applications/
