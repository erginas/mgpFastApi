from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.izin_sebebi import IzinSebebi, IzinSebebiCreate
from models.izin_sebebi import IzinSebebi as DBIzinSebebi
from crud.izin_sebebi import get_all_izin_sebebi, get_izin_sebebi_by_id, create_izin_sebebi

router = APIRouter(prefix='/izin_sebebi', tags=['IzinSebebi'])

@router.get('/', response_model=list[IzinSebebi])
async def list_izin_sebebi(db: AsyncSession = Depends()):
    return await get_all_izin_sebebi(db)

@router.get('/{id}', response_model=IzinSebebi)
async def get_izin_sebebi_item(id: int, db: AsyncSession = Depends()):
    result = await get_izin_sebebi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IzinSebebi)
async def create_izin_sebebi_item(data: IzinSebebiCreate, db: AsyncSession = Depends()):
    db_item = DBIzinSebebi(**data.dict())
    return await create_izin_sebebi(db, db_item)