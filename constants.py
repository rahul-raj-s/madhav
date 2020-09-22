import json
f = open('local_settings.json')
data = json.load(f)
f.close()

FONT_SIZE = data['fontSize']
THEME = data['theme']
THEME_SETUP = {
        'dark':{'bg':'#000','fg':'#ffffff','cursor':'#ffffff'},
        'light' : {'bg':'#ffffff','fg':'blue','cursor':'#000'}
        }

FILE_TYPES = (('text file','*.txt'),('text file','*.py'),('all files','*.*'))

PYTHON_KEYWORDS =['False','await','else','import','pass','None','break','except','in','raise','True',
'False','finally','is','return','and','continue','for','lambda','try','as','def','from','nonlocal','while'
'assert','del','global','not','with','async','elif','if','or','yield','class'
                ]

PYTHON_METHODS =['print','sum','input','open','max','min']