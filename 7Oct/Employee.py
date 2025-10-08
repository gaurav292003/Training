from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for Employee
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

# In-memory list of employees (just a plain list)
employees = [
    Employee(id=1, name="Alice Johnson", department="HR", salary=50000),
    Employee(id=2, name="Bob Smith", department="Engineering", salary=75000),
    Employee(id=3, name="Charlie Brown", department="Marketing", salary=60000)
]

# GET /employees — Return all employees
@app.get("/employees")
def get_employees():
    return employees

# GET /employees/{emp_id} — Get one employee by ID
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# POST /employees — Add a new employee
@app.post("/employees", status_code=201)
def add_employee(new_employee: Employee):
    for emp in employees:
        if emp.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees.append(new_employee)
    return new_employee

# PUT /employees/{emp_id} — Update employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_data: Employee):
    for idx, emp in enumerate(employees):
        if emp.id == emp_id:
            employees[idx] = updated_data
            return updated_data
    raise HTTPException(status_code=404, detail="Employee not found")

# DELETE /employees/{emp_id}
@app.delete("/employees/{emp_id}", status_code=204)
def delete_employee(emp_id: int):
    for idx, emp in enumerate(employees):
        if emp.id == emp_id:
            employees.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Employee not found")

# BONUS: GET /employees/count
@app.get("/employees/count")
def count_employees():
    return {"count": len(employees)}
