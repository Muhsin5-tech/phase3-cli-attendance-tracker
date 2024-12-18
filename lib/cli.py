import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/../../")))

import datetime
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
    print("\n--- Record Attendance ---")
    students = session.query(Student).all()
    if not students:
        print("No student found, please add a student first.")
        return
    
    print("\nSelect a student: ")
    for student in students:
        print(f"{student.id}. {student.name}. (Age: {student.age})")

    student_id = input("Enter student ID: ").strip()
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Invalid student ID, try again")
        return
    
    date_input = input("Enter the date (YYYY-MM-DD): ").strip()
    try:
        date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format, please use YYYY-MM-DD.")
        return
    
    status = input("Enter attendance status (present/absent): ")
    if status not in ["present", "absent"]:
        print("Invalid input, please use 'present' or 'absent'.")
        return
    
    new_attendance = Attendance(student_id=student.id, date=date, status=status)
    session.add(new_attendance)
    session.commit()
    print(f"Attendance recorded for {student.name} on {date} as {status}.")

def view_student_attendance():
    print("\n--- View Student Attendance ---")
    student_id = input("Enter student ID: ")
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found, try again")
        return
    
    attendances = session.query(Attendance).filter_by(student_id=student.id).all()
    if not attendances:
        print(f"No attencance records for {student.name}.")
        return
    
    print(f"\nAttendance records for {student.name}: ")
    for attendance in attendances:
        print(f"Date: {attendance.date}, Status: {attendance.status}")

def view_day_attendance():
    pass

def update_attendance():
    pass
    
if __name__ == "__main__":
    main_menu()