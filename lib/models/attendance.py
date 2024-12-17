from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from lib.models import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False) # 'present' or 'absent'
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    student = relationship("Student", back_populates="attendances")

    def __repr__(self):
        return f"<Attendance(id={self.id}, date{self.date}, status='{self.status}', student_id{self.student_id})>"
    