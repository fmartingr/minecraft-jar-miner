DEBUG = False

SHOW_SUMMARY = False

###
#   TEXTURES
###
TEXTURES_PATHS = ['jarfile/assets/minecraft/textures/']
TEXTURES_EXTRA_SIZES_MULTIPLIER = [2, 4, 6, 8]
TEXTURES_OUTPUT_PATH = 'textures'

###
#   ITEMS
###
ITEMS_FILES = []
ITEMS_JAVA_KEYWORDS = ['flintAndSteel', 'axeStone', 'swordDiamond']
ITEMS_PATTERN = "new (?P<code>[a-z]{2}\((?P<id>[1-9]{1,3}).*\"(?P<name>\w+)\"\))"

###
#   BLOCKS
###
BLOCKS_FILES = []
BLOCKS_JAVA_KEYWORDS = ['stonebrick']
BLOCKS_PATTERN = "new (?P<code>[a-z]{1,3}\((?P<id>[1-9]{1,3}).*\"(?P<name>\w+)\"\))"

###
#   LANGUAGES
###
LANGUAGES_PATH = 'jarfile/assets/minecraft/lang'
LANGUAGES_MASTER_KEYS = [
    'language.name',
    'language.region',
    'language.code',
]

###
#   ACHIEVEMENTS
###
ACHIEVEMENTS_FILES = []
ACHIEVEMENTS_JAVA_KEYWORDS = ['onARail', 'flyPig']
ACHIEVEMENTS_PATTERN = "new (?P<code>[a-z]{1,2}\((?P<id>[1-9]{1,3})\, \"(?P<name>\w+)\".*\))"

###
#   MOBS
###
MOBS_FILES = []
MOBS_JAVA_KEYWORDS = ['mob/']
MOBS_PATTERN = '(?P<full>\"mob/(?P<name>[a-zA-Z0-9]+)\.png\")'

###
#   BLACKLIST
###
CLASS_BLACKLIST = [
    'and', 'abs', 'all', 'any', 'bin', 'chr'
]
