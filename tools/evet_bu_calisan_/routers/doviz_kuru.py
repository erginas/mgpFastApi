from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.doviz_kuru import DovizKuru, DovizKuruCreate
from models.doviz_kuru import DovizKuru as DBDovizKuru
from crud.doviz_kuru import get_all_doviz_kuru, get_doviz_kuru_by_id, create_doviz_kuru

router = APIRouter(prefix='/doviz_kuru', tags=['DovizKuru'])

@router.get('/', response_model=list[DovizKuru])
async def list_doviz_kuru(db: AsyncSession = Depends()):
    return await get_all_doviz_kuru(db)

@router.get('/{id}', response_model=DovizKuru)
async def get_doviz_kuru_item(id: int, db: AsyncSession = Depends()):
    result = await get_doviz_kuru_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DovizKuru)
async def create_doviz_kuru_item(data: DovizKuruCreate, db: AsyncSession = Depends()):
    db_item = DBDovizKuru(**data.dict())
    return await create_doviz_kuru(db, db_item)