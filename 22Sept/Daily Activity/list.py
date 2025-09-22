'''numbers= [1,3,4,6,7]
print(numbers[0])
print(numbers[-1])'''

#Tuple Functions
fruits=['apple','banana','orange']
fruits.append('pear')
print(fruits)
fruits.insert(1, 'mango')
print(fruits)
fruits.remove('banana')
print(fruits)
fruits.pop()
print(fruits)

#Unpacking Tuple
person=('Gaurav', 22, 'Kolkata')
name, age, city = person
print(name)
print(age)
print(city)
