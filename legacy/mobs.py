#!/usr/bin/env python

# TODO

# General libs
import re
import json
import os
import sys

# Tool libs
from utils import run, sanitize
import utils
import conf
from objects import GameMob


utils.title('MOBS')


###
#   GLOBALS
###
ITEMS = []
ITEMS_STR = []

###
#   LOOK FOR CORRECT JAVA FILES
###
utils.sub("Looking for java files...")
#utils.sub("Keywords: %s" % ', '.join(conf.ACHIEVEMENTS_JAVA_KEYWORDS))
for keyword in conf.MOBS_JAVA_KEYWORDS:
    cmd = run("grep '%s' ./classes/*" % keyword)
    for result in cmd:
        for line in result.split('\n'):
            if line and result is not '':
                java_file = os.path.basename(line.strip().split()[0][:-1])
                if java_file not in conf.MOBS_FILES:
                    utils.echo("%s " % java_file, end='')
                    conf.MOBS_FILES.append(java_file)

utils.echo('\r')

###
#   GET ITEMS INFO FROM CLASSFILE
###
utils.sub('Looking for dataz', end='\n')

# TODO OLD Data

for java_file in conf.MOBS_FILES:
    print(java_file)
    file_handler = open('./classes/%s' % java_file)
    data = file_handler.read().split("\n")

    item_regex = re.compile(conf.MOBS_PATTERN)
    class_error_regex = re.compile('name \'(?P<name>\w+)\' is not defined')

    for line in data:
        if '"' in line:
            t = item_regex.search(line)
            if t:
                item = t.groupdict()
                if conf.DEBUG:
                    print("Line: " + item['name'])

                if item['name'] not in ITEMS_STR:
                    obj = GameMob(item['name'], item['full'])
                    ITEMS.append(obj)
                    ITEMS_STR.append(item['name'])

for x in ITEMS:
    print(x)
