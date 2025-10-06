import json
import logging

logging.basicConfig(filename='test.log',level=logging.INFO,format='%(asctime)s -%(levelname)s %(message)s')

students_data= [
    {"name": "Rahul", "age":21, "course":"AI", "marks": 85},
    {"name": "Priya", "age":22, "course":"ML", "marks": 90},
]

with open('students.json', 'w') as file:
    json.dump(students_data, file, indent=4)
logging.info("Initial students.json file created successfully")

try:
    with open('students.json', 'r') as file:
        students = json.load(file)
    logging.info("file read successfully")

    print("Student Names:")
    for student in students:
        print(student["name"])


    new_student={"name":"Arjun", "age": 20, "course":"Data Science", "marks": 85}
    students.append(new_student)
    logging.info("New Student added successfully")

    with open('students.json', 'w') as file:
        json.dump(students, file, indent=4)
    logging.info("File saved successfully")

except Exception as e:
    logging.error(f"Something went wrong: {e}")