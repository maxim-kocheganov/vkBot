import os
import configparser

class Settings:
    def __init__(self,keys,settings):
        fileToken = open(os.path.join(keys, 'token.txt'), "r")
        fileGroupID = open(os.path.join('keys', 'group.txt'), "r")
        self.basicToken = fileToken.read().split('\n')[0]
        self.groupID = fileGroupID.read().split('\n')[0]
        fileToken.close()
        fileGroupID.close()
        config = configparser.ConfigParser()
        config.read(os.path.join(settings,"config.ini"))
        try:
            self.debug = bool(config.get("debug","debug"))
        except (configparser.NoOptionError, configparser.NoSectionError):
            self.debug = False
        try:
            self.verbouse = bool(config.get("debug","verbouse"))
        except (configparser.NoOptionError, configparser.NoSectionError):
            self.verbouse = False
