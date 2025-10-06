from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    email: str
    isActive: bool = True

data= {"name":"Gaurav", "age":22, "email":"gaurav@gmail.com"}
student= Student(**data)

print(student)
print(student.name)

'''invalid_data= {"name":"Gaurav", "age":"tweenty", "email":"gaurav@gmail.com"}
student= Student(**invalid_data)'''
