cars = ['BMW', 'Mercedes', 'Opel', 'Mazda']
result = len(cars)
result = cars[0]
#result = cars[3]
#result = cars[-1]

cars[-1]= 'Toyota'
result = cars

result = 'Mercedes' in cars

result = cars[-2]
result = cars[0:3]
result = cars[:3]
result = cars[-2:]


cars[-2:] = ['Toyota', 'Renault']
result = cars

result = cars + ['Audi', 'Nissan']

del cars[-1]
result = cars


result = cars[::-1]

studentA = 'Kane', 'Jackson', 2010,[70,60,70]
studentB = 'Nuno', 'Gomes', 1999,[80,80,70]
studentC = 'Sofie', 'Anderson', 1998,[80,70,90]

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} years old and avarage of grade is {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"


print(result)
