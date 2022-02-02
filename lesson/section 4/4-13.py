a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
print(a)
print(type(a))
print('\n')

b = {2, 3, 3, 6, 7}
print(b)
print(a - b)    # aとbの差集合
print(b - a)    # bとaの差集合
print(a & b)    # aとbの積集合   ※a + bはTypeErrorになるので注意
print(a | b)    # aとbの和集合
print(a ^ b)    # aとbの非重複集合   各集合内で同じ要素を持たない要素の集合(積集合ではない！)