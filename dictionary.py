#key - value

'''
cities = ['Istanbul', 'Izmir']
plades = [34, 35]

print(plades[cities.index('Istanbul')]) 

plades = {'Istanbul' : 34, 'Izmir': 35}
print(plades['Istanbul'])
print(plades['Izmir'])

plades['Ankara'] = 6
plades['Istanbul'] = 'New value'

print(plades)
'''

users = {'menerglobal': {
         'age': 27,
         'email': 'mener@gmail.com',
         'address': 'Istanbul',
         'phone' : '77562343'
         },
         'angel': {
         'age': 32,
         'email': 'angel@gmail.com',
         'address': 'Izmir',
         'phone' : '73442343'
         }
}
print(users['angel']['age'])
