website = "http://www.menerglobal.com"
course = "Python course: From the beginning to the highest level for everyone"

'''
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()
'''
#result = website.lstrip('/:htp')

#result = 'www.menerglobal.com'.strip('w.').rstrip('.com')
#result = course.upper()

result = website.count('a')
result = website.count('www',0,10)
result = website.startswith('www')
result = website.endswith('com')
result = website.find('www')
result = website.index('com')


result = course.isalpha()
result = course.isdigit()
result = '123456789'.isdigit()

result = 'Contents'.center(50,'*')
result = 'Contents'.rjust(50,'*')
result = course.replace(' ', '-')

result = course.replace(' ', '-', 5)
result = course.replace(' ', '')


result = 'Hello World'.replace('World', 'There')

result = course.split(' ')

result = result[5]

print(result)
