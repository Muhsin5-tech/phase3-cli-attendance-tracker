# Placeholder for Student and Attendance models
from sqlalchemy import Column, Integer, String
from . import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, age={self.age})>"