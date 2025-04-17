from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aktar_sut_fiyat2 import AktarSutFiyat2, AktarSutFiyat2Create
from models.aktar_sut_fiyat2 import AktarSutFiyat2 as DBAktarSutFiyat2
from crud.aktar_sut_fiyat2 import get_all_aktar_sut_fiyat2, get_aktar_sut_fiyat2_by_id, create_aktar_sut_fiyat2

router = APIRouter(prefix='/aktar_sut_fiyat2', tags=['AktarSutFiyat2'])

@router.get('/', response_model=list[AktarSutFiyat2])
async def list_aktar_sut_fiyat2(db: AsyncSession = Depends()):
    return await get_all_aktar_sut_fiyat2(db)

@router.get('/{id}', response_model=AktarSutFiyat2)
async def get_aktar_sut_fiyat2_item(id: int, db: AsyncSession = Depends()):
    result = await get_aktar_sut_fiyat2_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AktarSutFiyat2)
async def create_aktar_sut_fiyat2_item(data: AktarSutFiyat2Create, db: AsyncSession = Depends()):
    db_item = DBAktarSutFiyat2(**data.dict())
    return await create_aktar_sut_fiyat2(db, db_item)