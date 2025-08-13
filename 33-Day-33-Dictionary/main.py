info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
# print(info['name2']) #KeyError: 'name2'
print(info.get('name2'))
print(info.get('name'))
print(info['age'])
print(info['eligible'])
print(info)
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}")