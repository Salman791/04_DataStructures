names = []
print(len(names))
names.append("William")
print(len(names))
names.append("John")
names.append("Amanda")
print(len(names))
print(names[2])

for i in names:
    print(i)

for i, j in enumerate(names):
    print(i + 1,"." ,j) #figure out how to print out the '.' without any space in between

for i in names:
    names.reverse()
print(names)

names.clear()
print(len(names))


