from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.database import SessionLocal
from core.dependencies import get_db
from .crud import kisi_listesi
from .models import Kisi

# from .schemas import EmployeeCreate, EmployeeUpdate, EmployeeOut
#from database import SessionLocal  # Veritabanı bağlantısını import ediyoruz

# Router oluşturuyoruz

router = APIRouter()

# Dependency: Veritabanı bağlantısı


# Yeni çalışan oluştur
@router.get("/kisi-list", response_model=List[Kisi])
async def get_kisi(kisi_listesi: List[Kisi] = Depends(kisi_listesi)):
    return kisi_listesi
#
# @router.post("/", response_model=EmployeeOut)
# def create_new_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
#     return create_employee(db=db, employee=employee)
#
# # Tüm çalışanları listele
#
# # ID ile çalışanı getir
# @router.get("/{employee_id}", response_model=EmployeeOut)
# def read_employee(employee_id: int, db: Session = Depends(get_db)):
#     db_employee = get_employee(db, employee_id=employee_id)
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return db_employee
#
# # Çalışan bilgilerini güncelle
# @router.put("/{employee_id}", response_model=EmployeeOut)
# def update_employee_details(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
#     db_employee = update_employee(db, employee_id=employee_id, employee=employee)
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return db_employee
#
# # Çalışanı sil
# @router.delete("/{employee_id}", response_model=EmployeeOut)
# def delete_employee_details(employee_id: int, db: Session = Depends(get_db)):
#     db_employee = delete_employee(db, employee_id=employee_id)
#     if db_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return db_employee
