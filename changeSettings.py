import json

def changeSettings(update:dict):
    f = open('local_settings.json','r')
    file_data = json.load(f)
    f.close()
    for new in update:
        file_data[new] = update[new]
    file_data = json.dumps(file_data, indent = 4) 
    with open("local_settings.json", "w") as outfile: 
            outfile.write(file_data) 