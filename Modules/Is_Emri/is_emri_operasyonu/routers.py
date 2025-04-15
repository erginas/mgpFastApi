from importlib import import_module

from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from sqlalchemy.orm import Session

from core.dependencies import get_session
from Modules.Is_Emri.is_emri_operasyonu.crud import *
from Modules.Is_Emri.is_emri_operasyonu.schemas import IsEmriOperasyonuOut, IsEmriOperasyonuBase, IsEmriOperasyonuCreate

router = APIRouter(prefix="/is-emri-operasyonu", tags=["İş Emri Operasyonu"])

# @router.get("/", response_model=List[IsEmriOperasyonuOut])
# async def list_is_emri_operasyonlari(session: AsyncSession = Depends(get_session)):
#     return await get_all_is_emri_operasyonlari(session)

# @router.get("/", response_model=List[IsEmriOperasyonuOut])
# async def list_is_emri_operasyonlari(
#     limit: int = 100,
#     session: AsyncSession = Depends(get_session)
# ):
#     return await get_all_is_emri_operasyonlari(session, limit)

@router.get("/{isemri_no}")
async def get_is_emri_operasyonlari(isemri_no: int):
    try:
        # Veritabanından veri çekme
        result = await get_is_emri_operasyonlari_raw(isemri_no)
        if not result:
            raise HTTPException(status_code=404, detail="İş emri operasyonları bulunamadı.")
        return result
    except Exception as e:
        print(f"Hata: {str(e)}")  # Loglama
        raise HTTPException(status_code=500, detail=f"Sunucu hatası: {str(e)}")

@router.get("/{islem_sirasi}/{operasyon_no}", response_model=IsEmriOperasyonuOut)
async def get_by_id(islem_sirasi: int, operasyon_no: int, session: AsyncSession = Depends(get_session)):
    item = await get_is_emri_operasyonu(session, islem_sirasi, operasyon_no)
    if not item:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı.")
    return item

@router.post("/", response_model=IsEmriOperasyonuOut)
async def create(data: IsEmriOperasyonuCreate, session: AsyncSession = Depends(get_session)):
    return await create_is_emri_operasyonu(session, data)

@router.put("/{islem_sirasi}/{operasyon_no}", response_model=IsEmriOperasyonuOut)
async def update(islem_sirasi: int, operasyon_no: int, data: IsEmriOperasyonuCreate, session: AsyncSession = Depends(get_session)):
    return await update_is_emri_operasyonu(session, islem_sirasi, operasyon_no, data)

@router.delete("/{islem_sirasi}/{operasyon_no}")
async def delete(islem_sirasi: int, operasyon_no: int, session: AsyncSession = Depends(get_session)):
    return await delete_is_emri_operasyonu(session, islem_sirasi, operasyon_no)
