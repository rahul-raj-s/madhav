import json 
  
# default settings
default_settings ={ 
    "theme" : "light", 
    "fontSize" : 10, 
} 
  
# Serializing json  
DEFAULT_SETTINGS = json.dumps(default_settings, indent = 4) 
  
