# from lesson_package.talk import animal
from lesson_package.talk import *   # *を使った場合はtalkの__init__.pyに__all__に記述が必要

print(animal.sing())
print(animal.cry())