from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kitaplar_kitap import KitaplarKitap, KitaplarKitapCreate
from models.kitaplar_kitap import KitaplarKitap as DBKitaplarKitap
from crud.kitaplar_kitap import get_all_kitaplar_kitap, get_kitaplar_kitap_by_id, create_kitaplar_kitap

router = APIRouter(prefix='/kitaplar_kitap', tags=['KitaplarKitap'])

@router.get('/', response_model=list[KitaplarKitap])
async def list_kitaplar_kitap(db: AsyncSession = Depends()):
    return await get_all_kitaplar_kitap(db)

@router.get('/{id}', response_model=KitaplarKitap)
async def get_kitaplar_kitap_item(id: int, db: AsyncSession = Depends()):
    result = await get_kitaplar_kitap_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KitaplarKitap)
async def create_kitaplar_kitap_item(data: KitaplarKitapCreate, db: AsyncSession = Depends()):
    db_item = DBKitaplarKitap(**data.dict())
    return await create_kitaplar_kitap(db, db_item)