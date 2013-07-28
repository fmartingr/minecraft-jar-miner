##
#   ITEM
##
class GameItem(object):
    def __init__(self, game_id, *args):
        self.id = int(game_id)

    def __str__(self, *args):
        return "<Item(%d: '%s')>" % (
            self.id,
            self.name
        )

    def method(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            "Sets the name"
            self.name = args[0]
        return self

    def __getattr__(self, *args):
        return self.method

##
#   BLOCK
##
class GameBlock(object):
    def __init__(self, game_id, *args):
        self.id = int(game_id)# + 256

    def __str__(self, *args):
        return "<Block(%d: '%s')>" % (
            self.id,
            self.name
        )

    def method(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            "Sets the name"
            self.name = args[0]
        return self

    def __getattr__(self, *args):
        return self.method

##
#   TEXTURE
##
class GameTexture(object):
    def __init__(self, name, typ, path):
        self.name = self.parse_name(name)
        self.path = path
        self.type = typ

    def __str__(self, *args):
        return "<Texture (%s: '%s')>" % (
            self.type,
            self.name
        )

    def full_name(self):
        return "%s.%s" % (self.type, self.name)

    def parse_name(self, name):
        return name.split('.')[0]


###
#   LANGUAGES
###
class GameLanguage(object):
    def __init__(self, name=None, region=None, code=None):
        self.name = name
        self.region = region
        self.code = code
        self.strings = {}

    def __str__(self):
        return "<Language (%s: '%s')>" % (
            self.code,
            self.name
        )

    def add_string(self, key, value):
        if key not in self.strings:
            self.strings[key] = value

###
#   ACHIEVEMENTS
###
class GameAchievement(object):
    def __init__(self, internal_id, name, *args):
        self.id = int(internal_id)
        self.name = name

    def method(self, *args):
        return self

    def __getattr__(self, *args):
        return self.method

    def __str__(self):
        return "<Achievement (%d: '%s')>" % (
            self.id,
            self.name
        )


###
#   MOBS
###
class GameMob(object):
    def __init__(self, name, full, *args):
        self.name = name
        self.full = full

    def method(self, *args):
        return self

    def __getattr__(self, *args):
        return self.method

    def __str__(self):
        return "<Mob (%s: '%s')>" % (
            self.name,
            self.full
        )
