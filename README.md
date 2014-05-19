minecraft-jar-miner
===================

**CURRENTLY UPDATING FOR 1.8 SNAPSHOT**

Used to get data for my test site [minecraftcodex.com](http://www.minecraftcodex.com)

# Requirements.txt

- fabric

# Commands

```
$ fab -l
Available commands:
    clean     Cleans decompiled and unpacked files for the specified version.
    unpack    Unpacks and decompiles classes for the specified version
    versions  List all detected versions
```

```
$ fab unpack:version=1.6.4
```

# Usage

TODO

# Configuration

TODO

# Parsers

TODO

Type | File | Status | Comment | Updated to
-----|------|--------|---------|-----------
Textures | textures.py | Base info | -- | --
Items | items.py | Base info | -- | --
Blocks | blocks.py | Base info | -- | --
Achievements | achievements.py | Only name | Need icons and inheritance | 1.7.2
Languages | languages.py | Need rewrite | Assets folder moved to launcher | --
Special items/blocks | -- | -- | -- | --
Potions | -- | -- | -- | --
Mobs | -- | -- | -- | --
Biomes | -- | -- | -- | --
Splash messages | -- | -- | -- | --
