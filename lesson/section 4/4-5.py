seat = []
min = 0
max = 5
print(min <= len(seat) < max)
seat.append('p')
print(min <= len(seat) < max)
print(len(seat))
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
seat.append('p')
seat.pop(0)
seat.pop(0)
print(min <= len(seat) < max)
print(len(seat))