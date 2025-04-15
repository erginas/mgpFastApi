from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.database import async_sessionmaker as get_db
from .crud import get_employees, create_employee, get_employee, update_employee, delete_employee
from .schemas import EmployeeCreate, EmployeeUpdate, EmployeeOut
#from database import SessionLocal  # Veritabanı bağlantısını import ediyoruz

# Router oluşturuyoruz

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

# Dependency: Veritabanı bağlantısı


# Yeni çalışan oluştur
@router.post("/", response_model=EmployeeOut)
def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db=db, employee=employee)

# Tüm çalışanları listele
@router.get("/", response_model=List[EmployeeOut])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = get_employees(db, skip=skip, limit=limit)
    return employees

# ID ile çalışanı getir
@router.get("/{employee_id}", response_model=EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Çalışan bilgilerini güncelle
@router.put("/{employee_id}", response_model=EmployeeOut)
def update_employee_details(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = update_employee(db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Çalışanı sil
@router.delete("/{employee_id}", response_model=EmployeeOut)
def delete_employee_details(employee_id: int, db: Session = Depends(get_db)):
    db_employee = delete_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
