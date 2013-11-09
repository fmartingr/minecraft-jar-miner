import subprocess
import re
from conf import CLASS_BLACKLIST
import random
import string
import sys
import os

def replace_classnames(code):
    char_set = string.ascii_lowercase
    result = code
    for item in CLASS_BLACKLIST:
        if "%s(" % item in result:
            rand = ''.join(random.sample(char_set*6,6))
            result = result.replace(item, rand)
    return result


def run(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = p.communicate()
    yield output


def sanitize(string):
    "Converts parameters and stuff to be correctly evaluated."
    # Remove class declarations in parameters
    regex = re.compile('new [\w]{1,3}(.*),')
    sane = regex.sub(r'', string)
    # Remove double parentesis
    sane = sane.strip().replace('))', ')')
    # Boolean values
    sane = sane.strip().replace('false', 'False')
    sane = sane.strip().replace('true', 'True')
    # Convert float values to string
    regex = re.compile('([\-]?\d?\.?\d\F)')
    sane = regex.sub("'\1'", sane)
    # Convert rest to string
    regex = re.compile('([, |\(])([\w+\d+\.]+)')
    sane = regex.sub(r'\1"\2"', sane)
    sane = replace_classnames(sane)
    return sane

# Functions
class Colors:
    END = '\033[0m'

    def __init__(self, c='ter,'):
        if c == 'custom':
            self.custom()
        else:
            self.term()

    def custom(self):
        self.WHITE = '\033[89m'
        self.BLACK = '\033[90m'
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.PURPLE = '\033[95m'
        self.CYAN = '\033[96m'

    def term(self):
        self.WHITE = '\033[29m'
        self.BLACK = '\033[30m'
        self.RED = '\033[31m'
        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'
        self.BLUE = '\033[34m'
        self.PURPLE = '\033[35m'
        self.CYAN = '\033[36m'

colors = Colors('custom')


def echo(string, end='\r\n', color=None):
    if color:
        sys.stdout.write("%s%s%s" % (
            color,
            string,
            colors.END
        ))
    else:
        sys.stdout.write(string)
    if end:
        sys.stdout.write("\n")
    sys.stdout.flush()


# Shortcurts
def check_status(status=None, words=['done', 'failed']):
    if status is not None:
        if status == 0:
            echo(words[0], color=colors.GREEN)
        else:
            echo(words[1], color=colors.RED)
            pass
            #exit(-1)


def exists(path):
    return os.path.exists(path)


def title(string):
    print("")
    echo("[==] %s" % string, color=colors.PURPLE)


def info(string):
    echo("[ i] %s" % string, color=colors.BLUE)


def error(string):
    echo("[ E] %s" % string, color=colors.RED)


def success(string):
    echo("[OK] %s" % string, color=colors.GREEN)


def sub(string, end='', color=None):
    echo("     %s " % string, end=end, color=color)
