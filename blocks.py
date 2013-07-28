#!/usr/bin/env python

# General libs
import re
import json
import os
import sys

# Tool libs
import utils
import conf
from objects import GameBlock


utils.title('BLOCKS')

###
#   GLOBALS
###
BLOCKS = []

###
#   LOOK FOR CORRECT JAVA FILES
###
utils.sub("Looking for java files...")
#utils.sub("Keywords: %s" % ', '.join(conf.BLOCKS_JAVA_KEYWORDS), end='\n')
for keyword in conf.BLOCKS_JAVA_KEYWORDS:
    command = utils.run('grep \'%s\' ./classes/*' % keyword)
    lines = []
    [lines.append(x) for x in command]
    lines = ''.join(lines).split('\n')
    for result in lines:
        if result and result is not '':
            java_file = os.path.basename(result.strip().split()[0][:-1])
            if java_file not in conf.BLOCKS_FILES:
                utils.echo("%s " % java_file, end='')
                conf.BLOCKS_FILES.append(java_file)

utils.echo('\r')

###
#   GET ITEMS INFO FROM CLASSFILE
###
utils.sub('Looking for dataz', end='\n')

# Old items for final count
try:
    OLD_BLOCKS = json.loads(open('blocks.json').read())
except:
    OLD_BLOCKS = {}
    OLD_BLOCKS['list'] = {}

for java_file in conf.BLOCKS_FILES:
    file_handler = open('./classes/%s' % java_file)
    data = file_handler.read().split("\n")

    item_regex = re.compile(conf.BLOCKS_PATTERN)
    class_error_regex = re.compile('name \'(?P<name>\w+)\' is not defined')

    for line in data:
        if '"' in line:  # Reduces iterations
            t = item_regex.search(line)
            if t:
                item = t.groupdict()
                if conf.DEBUG:
                    print("Line: " + item['code'])

                item['code'] = utils.sanitize(item['code'])

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
                        type(class_name, (GameBlock,), {}))
                    obj = eval(item['code'])

                if conf.DEBUG:
                    print("result object: " + obj.__str__())
                    print('- - - - - -')

                BLOCKS.append(obj)

# Print the miner summary and compile the new old data
new_old_data = {}
new_old_data['list'] = []
[new_old_data['list'].append(x.name) for x in BLOCKS]
new_blocks = len(new_old_data['list'])-len(OLD_BLOCKS['list'])
utils.info('Found %d blocks (%d new)' %
    (len(new_old_data['list']), new_blocks))
if conf.SHOW_SUMMARY:
    if new_blocks != 0:
        utils.sub('Modifications:', end='\n')
        for item in BLOCKS:
            if item.name not in OLD_BLOCKS['list']:
                utils.sub(' + %s' % item.name, end='\n',
                          color=utils.colors.GREEN)

        for item in OLD_BLOCKS['list']:
            if item not in new_old_data['list']:
                utils.sub(' - %s' % item, end='\n', color=utils.colors.RED)

oldblocks = open('blocks.json', 'w')
oldblocks.write(json.dumps(new_old_data))
