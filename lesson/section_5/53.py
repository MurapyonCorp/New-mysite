def menu(food, *args, **kwargs):
  print(food)
  print(args)
  print(kwargs)

menu('banana', 'orange', 'apple', entree='beef', drink='coffee')

# d = {
#   'entree': 'beef',
#   'drink': 'coffee',
#   'dessert': 'ice'
# }
# menu(**d)