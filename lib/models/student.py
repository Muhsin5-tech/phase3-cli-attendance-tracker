# Placeholder for Student and Attendance models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"