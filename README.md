# Class Attendance Tracker CLI

A Python-based Command-Line Interface (CLI) application for managing student attendance records, built using SQLAlchemy ORM.

## Features
- Add new students: Adds a student to the system with a name and age.
- Record attendance: Records the attendance (present/absent) for a student on a specific day.
- View attendance by student or by day: Display the attendance history of a particular student.
- View day attendances: Display attendance record for all students on a specific day.
- Update attendance: Allows you to update the attendance status for a specific student on a given date.

# Dependencies 
- SQLAlchemy
- Alembic
- Datetime

# installing
1. Clone repo:
    - git clone git@github.com:Muhsin5-tech/phase3-cli-attendance-tracker.git
    - cd phase3-cli-attendance-tracker
    - pipenv install - install dependencies
    - pipenv shell - activate environment
    - python -m lib.cli - start cli application

