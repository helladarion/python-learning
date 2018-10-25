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

class Save:
    def savedata(name, value):
        if os.path.isfile("./save.json") and os.stat("./save.json").st_size != 0:
            old_file = open("./save.json", "r+")
            data = json.loads(old_file.read())
            data["hp"] = value
            data["name"] = name
        else:
            old_file = open("./save.json","w+")
            data = {"name": "Jack", "hp": value}

        old_file.seek(0)
        old_file.write(json.dumps(data))

