import os
import simplejson as json

class bcolor:
    PURPLE      = '\033[35m'
    BLUE        = '\033[34m'
    GREEN       = '\033[32m'
    YELLOW      = '\033[33m'
    RED         = '\033[31m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'

class ascii_text:
    ACTION = """\
   ___      __  _             
  / _ |____/ /_(_)__  ___  ___
 / __ / __/ __/ / _ \/ _ \(_-<
/_/ |_\__/\__/_/\___/_//_/___/
                      """
    INVENTORY = """\
   ____                  __               
  /  _/__ _  _____ ___  / /____  ______ __
 _/ // _ \ |/ / -_) _ \/ __/ _ \/ __/ // /
/___/_//_/___/\__/_//_/\__/\___/_/  \_, / 
                                   /___/  
            """
    MAGIC = """\
   __  ___          _    
  /  |/  /__ ____ _(_)___
 / /|_/ / _ `/ _ `/ / __/
/_/  /_/\_,_/\_, /_/\__/ 
            /___/        
            """
    ENEMY_PHASE = """\
   ____                      ___  __               
  / __/__  ___ __ _  __ __  / _ \/ /  ___ ____ ___ 
 / _// _ \/ -_)  ' \/ // / / ___/ _ \/ _ `(_-</ -_)
/___/_//_/\__/_/_/_/\_, / /_/  /_//_/\_,_/___/\__/ 
                   /___/                           
            """
    AN_ENEMY_ATTACKS = """\
   ___          ____                      ___  __  __           __      
  / _ | ___    / __/__  ___ __ _  __ __  / _ |/ /_/ /____ _____/ /__ ___
 / __ |/ _ \  / _// _ \/ -_)  ' \/ // / / __ / __/ __/ _ `/ __/  '_/(_-<
/_/ |_/_//_/ /___/_//_/\__/_/_/_/\_, / /_/ |_\__/\__/\_,_/\__/_/\_\/___/
                                /___/                                   
            """
    def center_text():
        rows, cols = os.popen('stty size', 'r').read().split()
        middle_value = int(cols) // 2
        return middle_value

    def indent_ascii_text(indent_index,text,colour):
        lines = text.splitlines()
        half_text = len(lines[0]) // 2
        line_spaces = indent_index - half_text
        text_color = "bcolor." + colour
        for line in lines:
            print("{}{}{}{}".format(getattr(bcolor,colour),line_spaces * " ",line, bcolor.ENDC))
        return

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

