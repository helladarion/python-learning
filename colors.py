from classes.game import bcolor

print(bcolor.HEADER + "COLOR TEST" + bcolor.ENDC)
print(bcolor.OKBLUE + "COLOR TEST" + bcolor.ENDC)
print(bcolor.OKGREEN + "COLOR TEST" + bcolor.ENDC)
print(bcolor.WARNING + "COLOR TEST" + bcolor.ENDC)
print(bcolor.FAIL + "COLOR TEST" + bcolor.ENDC)
print(bcolor.BOLD + "COLOR TEST" + bcolor.ENDC)
print(bcolor.UNDERLINE + "COLOR TEST" + bcolor.ENDC)

def print_format_table():
        """
        prints table of formatted text format options
        """
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')

#print_format_table()
