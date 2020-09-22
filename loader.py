from default_setting import DEFAULT_SETTINGS

def haveLocalSettingFile():
    try:
        f = open('local_settings.json')
        f.close()
        return True
    except:
        return False
def configureSetups():
    print("here")
    if(not haveLocalSettingFile()):
        with open("local_settings.json", "w") as outfile: 
            outfile.write(DEFAULT_SETTINGS) 

configureSetups()
