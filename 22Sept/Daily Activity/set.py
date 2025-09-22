students= {"Gaurav", "Rahul", "Raj", "Rahul"}
print(students)

#Operations
fruits={"apple","banana","orange"}
print("apple" in fruits)
print("pear" in fruits)

set_a= {"Rahul", "Priya", "Raj", "Gaurav"}
set_b={"Rahul", "Amit", "Priya", "Dev"}

print(set_a | set_b) #Union
print(set_a & set_b) #Intersection
print(set_a - set_b) #Difference

#Getting unique values from list using set
names= ["Rahul", "Priya", "Raj", "Gaurav", "Rahul"]
unique_name= set(names)
print(unique_name)

