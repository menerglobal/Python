website = "http://www.menerglobal.com"
course = "Python course: From the beginnig to top level programming"
'''
result = len(course)
'''
'''
result = website[7:10]
'''

#lenght = len(website)

#result = website[23:26]
#result = website[lenght-3:lenght]

result = course[0:15]
result = course[:15]
result = course[-15:]

result = course[::-1]

print(result)


#s = '12345' * 5
#print(s[::5])

name , surname, age, job = 'Enes', 'Erdogan', 27, 'student'

result = "My name is " + name + " " + surname+ ", My age is "+ str(age)+ "and I am a " + job
result = "My name is {0} {1}. My age is {2} and I am a {3}.".format(name,surname,age,job)

result = f"My name is {name} {surname}. My age is {age} and I am a {job}."

s = 'Hello world'

s = s[0:6] + 'W' + s[-4:]
s.replace('w','W')
print(s)

result = 'abc ' * 3
print(result)

