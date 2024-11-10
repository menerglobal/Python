names = ['Aron', 'Maria', 'Cecilie', 'Håkan']
years = [1998, 2000, 1998, 1997]

#names.insert(4, 'Jack')
#names.insert(len(names), 'Jack')
#names.append('Jack')

#names.insert(0, 'Oliver')

'''
names.remove('Håkan')
names.pop()
names.pop(1)
'''

#index = names.index('Håkan')
#names.pop(index)

#result = 'Maria' in names
#result = names.index('Maria')
#print(result)

names.reverse()

names.sort()

#str = "Chevrolet,Dacia"
#result = str.split(',')
#print(result)

#min = min(years)
#max = max(years)
#print(min, max)

result = years.count(1998)

#years.clear()
#print(years)


print(names)


brands = []

brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)

brand = input("brand: ")
brands.append(brand)


print(brands)



