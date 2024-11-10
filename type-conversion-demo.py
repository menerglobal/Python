'''
Area of ​​circle : πr2
Circumference of circle : 2πr

Calculate the area and circumference of the circle. (r: 3.14)
'''

pi = 3.14

r = float(input("radius: "))
area = pi * (r ** 2)
circumference = 2 * pi * r

print("Area: "+ str(area) + " Circumference: "+ str(circumference))

