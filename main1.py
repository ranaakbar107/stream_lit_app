from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Ek fake database (list) data store karne ke liye
students_db = []

# Data ka format define karein (POST request ke liye)
class StudentData(BaseModel):
    name: str
    grade: str

# --- GET ROUTE ---
@app.get("/students")
def get_all_students():
    # Ye route students ki list return karega
    return {"total_students": len(students_db), "data": students_db}

# --- POST ROUTE ---
@app.post("/students", status_code=201)
def add_student(student: StudentData):
    # Naya student dictionary format mein banayein
    new_student_dict = {
        "id": len(students_db) + 1,
        "name": student.name,
        "grade": student.grade
    }
    
    # List mein add karein
    students_db.append(new_student_dict)
    
    return {"message": "Student add ho gaya!", "student": new_student_dict}