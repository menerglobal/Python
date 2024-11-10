numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49)
numbers.append(59)
numbers.insert(3, 78)
numbers.insert(-1, 52)

#numbers.pop(0)
#numbers.pop()
#numbers.pop(-1)

#numbers.remove(49)

numbers.sort()
letters.sort()

numbers.reverse()
letters.reverse()




print(len(letters))
print(len(numbers))


print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)
