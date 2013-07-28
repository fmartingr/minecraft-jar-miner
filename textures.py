#!/usr/bin/env python

# General libs
from os import listdir
from os.path import isfile, join
from sys import path
import json

# Tool libs
import utils
import conf
from objects import GameTexture


def read_dir(path, base_path):
    textures = []
    for item in listdir(path):
        if item != '.' and item != '..':
            if isfile(join(path, item)):
                typ = path.replace(base_path, '').replace('/', '.')
                model = GameTexture(
                    name=item,
                    typ=typ,
                    path=path
                )
                textures.append(model)
            else:
                [textures.append(x) for x in read_dir(
                    join(path, item), base_path)]
    return textures


utils.title("TEXTURES")

TEXTURES = []

# Old textures for final count
try:
    OLD_TEXTURES = json.loads(open('textures.json').read())
except:
    OLD_TEXTURES = {}
    OLD_TEXTURES['list'] = []


for current_path in conf.TEXTURES_PATHS:
    textures = read_dir(current_path, current_path)
    [TEXTURES.append(model) for model in textures]


# SUMMARY
new_old_data = {}
new_old_data['list'] = []
[new_old_data['list'].append(x.name) for x in TEXTURES]
new_items = len(new_old_data['list'])-len(OLD_TEXTURES['list'])
utils.info('Found %d textures (%d new)' % (len(TEXTURES), new_items))
if conf.SHOW_SUMMARY:
    if new_items != 0:
        utils.sub('Modifications', end='\n')
        for item in TEXTURES:
            if item.name not in OLD_TEXTURES['list']:
                utils.sub(' + %s' % item.name, end='\n',
                          color=utils.colors.GREEN)

        for item in OLD_TEXTURES['list']:
            if item not in new_old_data['list']:
                utils.sub(' - %s' % item, end='\n', color=utils.colors.RED)

olditems = open('textures.json', 'w')
olditems.write(json.dumps(new_old_data))
