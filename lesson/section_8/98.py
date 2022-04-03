import os

# print(os.path.exists('New-mysite/lesson/section_8/test.txt'))
# print(os.path.isfile('New-mysite/lesson/section_8/test.txt'))
# print(os.path.isdir('New-mysite/lesson/section_7'))
# os.rename('New-mysite/lesson/section_8/test.txt', 'New-mysite/lesson/section_8/renamed.txt')
os.symlink('New-mysite/lesson/section_8/renamed.txt', 'New-mysite/lesson/section_8/symlink.txt')