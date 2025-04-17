from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.cari_kayit import CariKayit, CariKayitCreate
from models.cari_kayit import CariKayit as DBCariKayit
from crud.cari_kayit import get_all_cari_kayit, get_cari_kayit_by_id, create_cari_kayit

router = APIRouter(prefix='/cari_kayit', tags=['CariKayit'])

@router.get('/', response_model=list[CariKayit])
async def list_cari_kayit(db: AsyncSession = Depends()):
    return await get_all_cari_kayit(db)

@router.get('/{id}', response_model=CariKayit)
async def get_cari_kayit_item(id: int, db: AsyncSession = Depends()):
    result = await get_cari_kayit_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=CariKayit)
async def create_cari_kayit_item(data: CariKayitCreate, db: AsyncSession = Depends()):
    db_item = DBCariKayit(**data.dict())
    return await create_cari_kayit(db, db_item)