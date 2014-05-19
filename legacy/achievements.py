#!/usr/bin/env python

# General libs
import re
import json
import os
import sys

# Tool libs
from utils import run, sanitize
import utils
import conf
from objects import GameAchievement


utils.title('ACHIEVEMENTS')

###
#   GLOBALS
###
ITEMS = []

###
#   LOOK FOR CORRECT JAVA FILES
###
utils.sub("Looking for java files...")
#utils.sub("Keywords: %s" % ', '.join(conf.ACHIEVEMENTS_JAVA_KEYWORDS))
for keyword in conf.ACHIEVEMENTS_JAVA_KEYWORDS:
    cmd = run('grep \'%s\' ./classes/*' % keyword)
    for result in cmd:
        if result and result is not '':
            java_file = os.path.basename(result.strip().split()[0][:-1])
            if java_file not in conf.ACHIEVEMENTS_FILES:
                utils.echo("%s " % java_file, end='')
                conf.ACHIEVEMENTS_FILES.append(java_file)

utils.echo('\r')

###
#   GET ITEMS INFO FROM CLASSFILE
###
utils.sub('Looking for dataz', end='\n')

# Old items for final count
try:
    OLD_ITEMS = json.loads(open('achievements.json').read())
except:
    OLD_ITEMS = {}
    OLD_ITEMS['list'] = []

for java_file in conf.ACHIEVEMENTS_FILES:
    file_handler = open('./classes/%s' % java_file)
    data = file_handler.read().split("\n")

    item_regex = re.compile(conf.ACHIEVEMENTS_PATTERN)
    class_error_regex = re.compile('name \'(?P<name>\w+)\' is not defined')

    for line in data:
        if '"' in line:
            t = item_regex.search(line)
            if t:
                item = t.groupdict()
                if conf.DEBUG:
                    print("Line: " + item['code'])

                item['code'] = sanitize(item['code'])

                if conf.DEBUG:
                    print("Sanitize: " + item['code'])

                try:
                    obj = eval(item['code'])
                except NameError as error:
                    # Create class for the given classname
                    class_name = class_error_regex.search(error.__str__())\
                        .group('name')
                    if conf.DEBUG:
                        print("Classname: %s" % class_name)
                    setattr(
                        sys.modules[__name__],
                        class_name,
                        type(class_name, (GameAchievement,), {}))
                    obj = eval(item['code'])
                #if obj.name == 'appleGold':
                if conf.DEBUG:
                    print("result object: " + obj.__str__())
                    print('- - - - - -')

                ITEMS.append(obj)

# Print the miner summary and compile the new old data
new_old_data = {}
new_old_data['list'] = []
[new_old_data['list'].append(x.name) for x in ITEMS]
new_items = len(new_old_data['list'])-len(OLD_ITEMS['list'])
utils.info('Found %d achievements (%d new)' %
    (len(new_old_data['list']), new_items))
if conf.SHOW_SUMMARY:
    if new_items != 0:
        utils.sub('Modifications:', end='\n')
        for item in ITEMS:
            if item.name not in OLD_ITEMS['list']:
                utils.sub(' + %s' % item.name, end='\n',
                          color=utils.colors.GREEN)

        for item in OLD_ITEMS['list']:
            if item not in new_old_data['list']:
                utils.sub(' - %s' % item, end='\n', color=utils.colors.RED)

olditems = open('achievements.json', 'w')
olditems.write(json.dumps(new_old_data))
