from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PublicHoliday(Base):
    __tablename__ = 'public_holidays'

    holiday_id = Column(Integer, primary_key=True, autoincrement=True)
    holiday_date = Column(Date, nullable=False)
    description = Column(String(100))

