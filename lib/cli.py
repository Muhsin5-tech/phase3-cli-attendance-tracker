import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../../")))


from lib.helper.seed_data import seed_data
from lib.models.student import Student
from lib.models.attendance import Attendance
from database import session

def main_menu():
    while True:
        print("\n=== Class Attendance Tracker ===")
        print("1. Add a new student")
        print("2. Record attendance")
        print("3. View attendance for a student")
        print("4. View attendance for a specific day")
        print("5. Update attendance record")
        print("6. Exit")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_student()
        elif choice == "2":
            record_new_student()
        elif choice == "3":
            view_student_attendance()
        elif choice == "4":
            view_day_attendance()
        elif choice == "5":
            update_attendance()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again please.")

def add_new_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    if not name or not age.isdigit():
        print("Invalid input, try again please.")
        return
    age = int(age)

    existing_student = session.query(Student).filter_by(name=name, age=age).first()
    if existing_student:
        print(f"Student '{name}' already exists")
    else:
        new_student = Student(name=name, age=age)
        session.add(new_student)
        session.commit()
        print(f"Student '{name}' added successfully!")

def record_new_student():
    pass 

def view_student_attendance():
    pass

def view_day_attendance():
    pass

def update_attendance():
    pass
    
if __name__ == "__main__":
    main_menu()