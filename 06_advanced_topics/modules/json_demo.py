import json

"""
json 模块演示
"""

print('\n----------- 将 JSON 对象转换成字符串 -----------')
obj = {'name': '54pig', 'age': 30}
s = json.dumps(obj)
print(s)

print('\n----------- 将字符串转换成 JSON 对象 -----------')
s = '{"name": "54pig", "age": 30}'
obj = json.loads(s)
print(obj['name'])

print('\n----------- 将 JSON 对象转换成字符串，并写入到文件中 -----------')
file = open('/tmp/python/person.json', 'w')
obj = {'name': '54pig', 'age': 30}
json.dump(obj, file)
file.close()

print('\n----------- 将读取文件中的字符串，转换成 JSON 对象 -----------')
file = open('/tmp/python/person.json')
obj = json.load(file)
print(obj)
print(obj['name'])
print(obj['age'])
file.close()
