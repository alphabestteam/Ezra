import json


config_json = open("Ezra/File Handling/4/config.json", "r")

p_config_json = json.load(config_json)

data_upper = p_config_json["data"].upper()

if p_config_json["silent"] == True:
    print(data_upper)

p_config_json["data"] = data_upper

# writing back in
config_json = open("Ezra/File Handling/4/config.json", "w")
config_json.write(json.dumps(p_config_json))

config_json.close()


