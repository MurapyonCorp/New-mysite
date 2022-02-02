d = {'x': 10, 'y': 20}
print(d)
print(d.keys())
print(d.values())
d2 = {'x': 1000, 'j': 500}
d.update(d2)
print(d)
print(d.get('x'))
print(d.pop('x'))
print(d)
del d['y']
print(d)
del d
# print(d)
d = {'a': 10, 'b': 20}
print(d)
d.clear()
print(d)
d = {'a': 10, 'b': 20}
print('a' in d)
print('j' in d)