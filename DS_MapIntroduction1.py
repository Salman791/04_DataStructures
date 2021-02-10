map = {}

print(len(map))

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

# map[97,98,99,65,66,67] = "a", "b", "c", "A", "B", "C" # wrong!
# print(map)

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

map[97] = 'a'
map[98] = 'b'
map[99] = 'c'
map[65] = 'A'
map[66] = 'B'
map[67] = 'C'
print(map)

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

print(map.keys())

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

print(map.values())

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

map[68] = "D"
print(map)

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

print(len(map))

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

value_of_key_99 = map[99]
print(value_of_key_99)

print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')

del map[97]
print(map)

for key,value in map.items():
    if key == 100:
        print(map[100])
    else:
        print("No such key exists")
    break
map.clear()
print(map)

