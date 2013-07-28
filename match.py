#!/usr/bin/env python

############################################################################
############################################################################
############################################################################
#
# THIS FILE IS USED ONLY FOR TESTING PURPOSES
#
############################################################################
############################################################################
############################################################################

import re
import json
from pprint import pprint

###
#   CONFIGURATION
###

DEBUG = True

ITEMS_FILE = 'wk.java'
BLOCKS_FILE = 'apa.java'

#bL = (new xc(135, 4, 0.6F, apa.ch.cz, apa.aE.cz)).b("carrots");
#bM = (new xc(136, 1, 0.3F, apa.ci.cz, apa.aE.cz)).b("potato");
#bO = (new wf(138, 2, 0.3F, false)).a(mk.u.H, 5, 0, 0.6F).b("potatoPoisonous");
#bQ = (new wf(140, 6, 1.2F, false)).b("carrotGolden").c(xu.l);
ITEMS_PATTERN = "new [a-z]{2}\((?P<id>[1-9]{1,3})[, (?P<hunger>\d+)]?.*\"(?P<name>\w+)\""
BLOCKS_PATTERN = ITEMS_PATTERN

###
#   GLOBALS
###
BLOCKS = []
ITEMS = []

###
#   GET ITEMS INFO FROM CLASSFILE
###
print("=> Mining items")
# Old items for final count
try:
    olditems = open('items.json').read()
    OLD_ITEMS = len(json.loads(olditems))
except:
    OLD_ITEMS = 0

file_handler = open('./classes/%s' % ITEMS_FILE)
data = file_handler.read().split("\n")

item_regex = re.compile(ITEMS_PATTERN)

for line in data:
    if '"' in line:
        if DEBUG:
            print(line)
        t = item_regex.search(line)
        if t:
            item = {
                'line': t.group(0).strip(),
                'code_id': int(t.group('id')),
                'id': int(t.group('id')) + 1 + 255,
                'internal_name': t.group('name')
            }
            item = t.groupdict()
            if DEBUG:
                print(item)

            ITEMS.append(item)
print('Fetched %d items (%d new)' % (len(ITEMS), abs(OLD_ITEMS-len(ITEMS))))

olditems = open('items.json', 'w')
olditems.write(json.dumps(ITEMS))
