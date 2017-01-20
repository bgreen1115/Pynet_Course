import yaml
import json
import pprint

list = range(5)
list.append('Item 1')
list.append('Item 2')
list.append({})
list[-1]['Name'] = 'Jim'
list[-1]['Age'] = 42

with open('list_file.yml', 'w') as f:
    f.write(yaml.dump(list, default_flow_style=True))
    f.close()

with open('json_list_file.json', 'w') as f:
    f.write(json.dumps(list))
    f.close()

