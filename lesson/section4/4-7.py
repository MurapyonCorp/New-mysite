num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
print('\n')

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = 'Mike', 'l', 'L', 'emma', 'e', 'F'

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)
# 数値を入れ替えるのに3行も書かないといけない
print('\n')

a = 100
b = 200
a, b = b, a
print(a, b)