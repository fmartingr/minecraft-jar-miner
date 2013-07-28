minecraft-jar-miner
===================

Extract minecraft information from its jarfiles. Used in my test site [minecraftcodex.com](http://www.minecraftcodex.com)

**Note:** The languages task is currently unimplemented since Mojang moved the language assets from the jarfile to the launcher folder which varies between operating systems. Will be reimplemented Soon™.

# Usage
Get the jarfile from the version you want to extract information, an place them in the folder, or specify a full path to it as argument:

```
$ ./run.sh 1.6.2.jar
[] Preparing files from JAR: 1.6.2.jar []
    Unpackaging jar file
    Decompiling classes
    Cleaning

[==] TEXTURES
[ i] Found 875 textures (875 new)

[==] ITEMS
     Looking for java files:  yb.java
     Looking for dataz
[ i] Found 169 items (169 new)

[==] BLOCKS
     Looking for java files... aqw.java
     Looking for dataz
[ i] Found 160 blocks (160 new)

[==] ACHIEVEMENTS
     Looking for java files... ko.java
     Looking for dataz
[ i] Found 24 achievements (24 new)
```

The script will create a json for each task for comparing every time you run the miner.

# Configuration file (conf.py)


- **DEBUG**: Show a little more information when extracting. Using for developing.  
- **SHOW SUMMARY**: Shows which items have been added/deleted from the current version comparing the json output files from the last jar you mined.

# Parsers

Type | File | Status | Comment
--|--|--|--
Textures | textures.py | Base info
Items | items.py | Base info
Blocks | blocks.py | Base info
Achievements | achievements.py | Base info | Need icons and inheritance
Languages | languages.py | Need rewrite | Assets folder moved to launcher
Special items/blocks | -- | --
Potions | -- | --
Mobs | -- | --
Biomes | -- | --
Splash messages | -- | --
