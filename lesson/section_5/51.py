def test_func(x, l=None):
  l.append(x)
  return l

y = [1, 2, 3]
r = test_func(100, y)
print(r)