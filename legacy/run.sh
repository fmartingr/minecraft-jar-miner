#!/bin/bash

./decompile.sh $1

python textures.py

python items.py

python blocks.py

# Need to use the minecraft installation folder
#python languages.py

python achievements.py
