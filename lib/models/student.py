# Placeholder for Student and Attendance models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    attendances = relationship("Attendance", back_populates="student")
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"