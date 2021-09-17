import json

data = {
    'no': 1,
    'name': 'Nowcoder',
    'url': 'http://www.nowcoder.com'
}

json_str = json.dumps(data)

print(json_str)
print(json.loads(json_str))
sample