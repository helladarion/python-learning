import os
import simplejson as json

class bcolor:
    HEADER      = '\033[35m'
    OKBLUE      = '\033[34m'
    OKGREEN     = '\033[32m'
    WARNING     = '\033[33m'
    FAIL        = '\033[31m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

class Persistence:
    def savedata(file, data):
        # Creating directory for saving stuff
        directory = os.path.dirname("assets/")
        if not os.path.exists(directory):
            os.makedirs("assets/")
        if os.path.isfile("assets/" + file) and os.stat("assets/" + file).st_size != 0:
            old_file = open("assets/" + file, "r+")
            data = json.loads(old_file.read())
        else:
            old_file = open("assets/" + file,"w+")

        old_file.seek(0)
        old_file.write(json.dumps(data))

    def load(file):
        if os.path.isfile("assets/" + file) and os.stat("assets/" + file).st_size != 0:
            old_file = open("assets/" + file, "r+")
            data = json.loads(old_file.read())
        else:
            data = []
        return data

