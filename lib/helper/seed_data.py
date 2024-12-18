import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from database import session
from lib.models.student import Student
from lib.models.attendance import Attendance

def seed_data():
    if session.query(Student).count() > 0:
        print("Already exists.Skipping this data insertion")
        return
    # Add sample students
    student1 = Student(name="Muhsin", age=18)
    student2 = Student(name="Ali", age=19)
    student3 = Student(name="Abdullahi", age=20)
    
    # Add all to the session
    session.add_all([student1, student2, student3])
    session.commit()
    
    print("Seed data added successfully!")
    
    # Query and display the data
    students = session.query(Student).all()
    print("Current students in the database:")
    for student in students:
        print(student)

if __name__ == "__main__":
    seed_data()
