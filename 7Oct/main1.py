from fastapi import FastAPI

app= FastAPI()

@app.get("/students")
def get_students():
    return{"message": "This is a GET request"}

@app.post("/students")
def create_student():
    return {"message": "This is a POST request"}

@app.put("/students")
def update_student(s):
    return {"This is a PUT request"}

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"This is a DELETE request"}