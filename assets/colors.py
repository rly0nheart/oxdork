import sys

colors = True
machine = sys.platform # Detecting the os of current system
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False # Colors will not be displayed in mac & windows
if not colors:
    end = red = white = green = yellow = cbg = brightred = ''
else:
    white = "\x1b[97m"
    green = "\x1b[92m"
    red = "\x1b[91m"
    end = "\x1b[0m"
    redbg = "\x1b[0;37;41m"
    greenbg = "\x1b[42;97m"
    brightred = "\x1b[31;1m"
    yellow = "\x1b[93m"
   
