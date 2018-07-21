import json

f = open('./json_load_test/sample.json', 'r')
json_dict = json.load(f)
print('json_dict:{}'.format(type(json_dict)))
