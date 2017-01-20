import json
import yaml
import pprint

with open('list_file.yml') as f:
    new_list = yaml.load(f)
    pprint.pprint(new_list)
    f.close()

with open('json_list_file.json') as f:
    new_list = json.load(f)
    pprint.pprint(new_list)
    f.close()
