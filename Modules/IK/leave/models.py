from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import enum


from core.database import engine

Base = declarative_base()

class LeaveType(enum.Enum):
    annual = "Annual"
    sick = "Sick"
    unpaid = "Unpaid"


class Leave(Base):
    __tablename__ = 'leaves'

    leave_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.employee_id'), nullable=False)
    leave_type = Column(String(50), nullable=False)  # Örnek: Yıllık, Hastalık
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String(20), default='Pending')  # İzin durumu
    used_days = Column(Integer, default=0)
    remaining_days = Column(Integer, default=0)
    year = Column(Integer, nullable=False)  # Yıl
    carried_over_days = Column(Integer, default=0)  # Biriken izinler
    official_holidays_excluded = Column(Integer, default=0)  # Resmi tatil günlerinin sayısı

    # İlişki
    employee = relationship('Employee', back_populates='leaves')
