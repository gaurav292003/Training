student={"name": "Alice",
        "age": 22,
        "course": "AIML"}

print(student["name"])
print(student.get("name"))

student["grade"]= "A"
student["age"]= 21

student.pop("course")
del student["grade"]
print(student)

for key,values in student.items():
    print(key, ":" , values)

#Nested Data
employee={
    "name": "Alice",
    "age": 22,
    "city": "San Jose",
    "skills" : ["Python", "Java", "C"]
}
print(employee["skills"][1])
