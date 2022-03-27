# import lesson_package.utils

# r = lesson_package.utils.say_twice('hello')
# print(r)

from lesson_package import utils as u

r = u.say_twice('hello')
print(r)

# from lesson_package.utils import say_twice

# r = say_twice('hello')
# print(r)