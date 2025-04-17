from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.rapor_yeni import RaporYeni, RaporYeniCreate
from models.rapor_yeni import RaporYeni as DBRaporYeni
from crud.rapor_yeni import get_all_rapor_yeni, get_rapor_yeni_by_id, create_rapor_yeni

router = APIRouter(prefix='/rapor_yeni', tags=['RaporYeni'])

@router.get('/', response_model=list[RaporYeni])
async def list_rapor_yeni(db: AsyncSession = Depends()):
    return await get_all_rapor_yeni(db)

@router.get('/{id}', response_model=RaporYeni)
async def get_rapor_yeni_item(id: int, db: AsyncSession = Depends()):
    result = await get_rapor_yeni_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=RaporYeni)
async def create_rapor_yeni_item(data: RaporYeniCreate, db: AsyncSession = Depends()):
    db_item = DBRaporYeni(**data.dict())
    return await create_rapor_yeni(db, db_item)