#!/usr/bin/env python

# General libs
import re
import json
import os
import sys

# Tool libs
import utils
import conf
from objects import GameLanguage


utils.title('LANGUAGES')
if conf.SAVE:
    sys.path.append('../../minecraftcodex')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'local_settings'
    from database.models import Language, LanguageString

###
#   GLOBALS
###
STRINGS = []
LANGUAGES = []
LANGUAGES_STR = []

###
#   LOOK FOR CORRECT JAVA FILES
###
utils.sub("Looking for languages files:")
directory_list = os.listdir(conf.LANGUAGES_PATH)
utils.echo("found %d file(s)" % len(directory_list), end='\n')

###
#   GET LANGUAGES
###
try:
    OLD_STRINGS = json.loads(open('strings.json').read())
except:
    OLD_STRINGS = []
try:
    OLD_LANGUAGES = json.loads(open('languages.json').read())
except:
    OLD_LANGUAGES = []

utils.sub('Looking for dataz', end='\n')
for item in directory_list:
    if '.lang' in item:
        if conf.DEBUG:
            print("      Now %s " % item)

        language = open('%s/%s' % (conf.LANGUAGES_PATH, item))
        language_obj = GameLanguage()
        for line in language.readlines():
            line = line.strip()
            if line and 'X-Generator' not in line:
                key, value = line.split('=', 1)
                if key in conf.LANGUAGES_MASTER_KEYS:
                    # Language object
                    setattr(language_obj, key.split('.')[1], value)
                else:
                    # Language String object
                    language_obj.add_string(key, value)

                    # Store for comparision
                    if language_obj.code == 'en_US':
                        if key not in STRINGS:
                            STRINGS.append(key)
        LANGUAGES.append(language_obj)

if conf.SAVE:
    for item in LANGUAGES:
        try:
            obj = Language.objects.get(
                name=item.name,
                region=item.region,
                code=item.code
            )
        except Language.DoesNotExist:
            obj = Language(
                name=item.name,
                region=item.region,
                code=item.code
            )
            obj.save()
        for key in item.strings.keys():
            value = item.strings[key]
            try:
                string_obj = LanguageString.objects.get(
                    language=obj,
                    key=key
                )
                if string_obj.value != value:
                    string_obj.value = value
                    string_obj.save()
            except LanguageString.DoesNotExist:
                string_obj = LanguageString(
                    language=obj,
                    key=key,
                    value=value
                )
                string_obj.save()


# LANGUAGES
[LANGUAGES_STR.append(x.name) for x in LANGUAGES]
new_languages = len(LANGUAGES_STR) - len(OLD_LANGUAGES)
utils.info("Found %d languages (%d new)." % (len(LANGUAGES_STR), new_languages))
if len(LANGUAGES_STR) != len(OLD_LANGUAGES):
    utils.sub('Modifications:', end='\n')

    for lang in LANGUAGES_STR:
        if lang not in OLD_LANGUAGES:
            utils.sub(' + %s' % lang, end='\n', color=utils.colors.GREEN)

    for lang in OLD_LANGUAGES:
        if lang not in LANGUAGES_STR:
            utils.sub(' - %s' % lang, end='\n', color=utils.colors.RED)

olditems = open('languages.json', 'w')
olditems.write(json.dumps(LANGUAGES_STR))
olditems.close()

# STRINGS
new_strings = len(STRINGS) - len(OLD_STRINGS)
utils.info("Found %d strings (%d new) -based on en_US-." % (len(STRINGS), new_strings))
if len(STRINGS) != len(OLD_STRINGS):
    utils.sub('Modifications:', end='\n')

    for string in STRINGS:
        if string not in OLD_STRINGS:
            utils.sub(' + %s' % string, end='\n', color=utils.colors.GREEN)

    for string in OLD_STRINGS:
        if string not in STRINGS:
            utils.sub(' - %s' % string, end='\n', color=utils.colors.RED)
            
olditems = open('strings.json', 'w')
olditems.write(json.dumps(STRINGS))
olditems.close()
