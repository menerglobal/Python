list = [1, 2, 3]

tuple = (1, 'iki', 3)
'''
print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(tuple))
print(len(list))
'''
list = ['Harry', 'Henry']
tuple = ('Rikke', 'Mette')
names = ('Frederik', 'Nikolas') + tuple

###list[0] = 'Younes' (possible)
###tuple[0] = 'Mary' (impossible)

print(tuple.count('Rikke'))
print(tuple.index('Rikke'))

print(list)
print(tuple)
print(names)
