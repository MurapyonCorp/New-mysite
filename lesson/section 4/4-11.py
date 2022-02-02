x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)
# 上記は参照渡しであり、xのキーの値が変わってしまう
print('\n')

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)