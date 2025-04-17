from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.urun_alternatifi import UrunAlternatifi, UrunAlternatifiCreate
from models.urun_alternatifi import UrunAlternatifi as DBUrunAlternatifi
from crud.urun_alternatifi import get_all_urun_alternatifi, get_urun_alternatifi_by_id, create_urun_alternatifi

router = APIRouter(prefix='/urun_alternatifi', tags=['UrunAlternatifi'])

@router.get('/', response_model=list[UrunAlternatifi])
async def list_urun_alternatifi(db: AsyncSession = Depends()):
    return await get_all_urun_alternatifi(db)

@router.get('/{id}', response_model=UrunAlternatifi)
async def get_urun_alternatifi_item(id: int, db: AsyncSession = Depends()):
    result = await get_urun_alternatifi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UrunAlternatifi)
async def create_urun_alternatifi_item(data: UrunAlternatifiCreate, db: AsyncSession = Depends()):
    db_item = DBUrunAlternatifi(**data.dict())
    return await create_urun_alternatifi(db, db_item)