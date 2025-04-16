from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from core.database import SessionFactory as get_db


router = APIRouter()


# Veri tabanına bağlanma



# İzin listeleme
@router.get("/leaves", response_model=List[schemas.Leave])
def get_leaves(db: Session = Depends(get_db)):
    leaves = db.query(models.Leave).all()
    return leaves


# Yeni izin talebi ekleme
@router.post("/leaves", response_model=schemas.Leave)
def create_leave(leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    db_leave = models.Leave(**leave.dict())
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave


# İzin güncelleme
@router.put("/leaves/{leave_id}", response_model=schemas.Leave)
def update_leave(leave_id: int, leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    db_leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
    if not db_leave:
        raise HTTPException(status_code=404, detail="Leave not found")

    for key, value in leave.dict().items():
        setattr(db_leave, key, value)

    db.commit()
    db.refresh(db_leave)
    return db_leave


# İzin silme
@router.delete("/leaves/{leave_id}", response_model=schemas.Leave)
def delete_leave(leave_id: int, db: Session = Depends(get_db)):
    db_leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
    if not db_leave:
        raise HTTPException(status_code=404, detail="Leave not found")

    db.delete(db_leave)
    db.commit()
    return db_leave
