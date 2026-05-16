from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    name: str = "raghuveer"
    age: Optional[int] = None
    grade: Optional[str] = None
    # email: EmailStr
    cgpa: float = Field(ge=0.0, le=10.0, default=0.0, description="CGPA must be between 0.0 and 10.0")

new_student = {
    "name": "raghuveer",
    "age": 25,
    "cgpa": 9
}

student = Student(**new_student)
student_dict = dict(student)
student_json = student.model_dump_json()

print("Student pydantic is: ",student)
print("Student dict is: ",student_dict)
print("Student JSON is: ",student_json)