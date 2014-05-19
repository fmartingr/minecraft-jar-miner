import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

###
# GENERAL
###

VERSIONS_PATH = os.path.join(BASE_DIR, 'versions')

###
# APPLICATIONS
###

# Java Decompiler
# ./tools/jad/jad -sjava -dclasses file.class
JAD = os.path.join(BASE_DIR, 'tools/jad/jad')
JAD_ARGS = '-sjava -d {destination}'

UNZIP = 'unzip'
UNZIP_ARGS = '-qq {jarfile} -d {destination}'

###
# OTHER
###


###
# LOCAL CONFIG
###

try:
    from local_config import *
except:
    pass
