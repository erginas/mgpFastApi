from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kullanici_form import KullaniciForm, KullaniciFormCreate
from models.kullanici_form import KullaniciForm as DBKullaniciForm
from crud.kullanici_form import get_all_kullanici_form, get_kullanici_form_by_id, create_kullanici_form

router = APIRouter(prefix='/kullanici_form', tags=['KullaniciForm'])

@router.get('/', response_model=list[KullaniciForm])
async def list_kullanici_form(db: AsyncSession = Depends()):
    return await get_all_kullanici_form(db)

@router.get('/{id}', response_model=KullaniciForm)
async def get_kullanici_form_item(id: int, db: AsyncSession = Depends()):
    result = await get_kullanici_form_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KullaniciForm)
async def create_kullanici_form_item(data: KullaniciFormCreate, db: AsyncSession = Depends()):
    db_item = DBKullaniciForm(**data.dict())
    return await create_kullanici_form(db, db_item)