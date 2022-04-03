s = """\
AAA
BBB
CCC
DDD
"""
# with open('New-mysite/lesson/section_8/test.txt', 'w') as f:
#   f.write(s)
  # print('My', 'name', 'is', 'Mike', sep = '#', end = '!', file = f)

with open('New-mysite/lesson/section_8/test.txt', 'r') as f:
  # print(f.read())
  while True:
    chunk = 2
    line = f.read(chunk)
    print(line)
    if not line:
      break
