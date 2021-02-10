ListA = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
print(ListA)
ListB = ListA.copy()
print(ListA[3])
ListB.remove('Durian') # How do I prevent it from deleting it in List A as well???
print('List B: ' + str(ListB))

ListA.append('Kiwi') # code will change if 'Durian' isn't deleted from List A!!!
print('List A: ' + str(ListA))

print('Length of List A: ' + str(len(ListA)) + ' v/s ' + 'Length of List B: ' + str(len(ListB)))

print(ListA.index('Avocado'))

for i in ListB:
    if i == 'Durian':
        print(i)
    else:
        print("'Durian' doesn't exist in List B anymore!")
    break

ListB.extend(('Passion Fruit', 'Pomelo'))
print(ListB)

print(ListA[2])