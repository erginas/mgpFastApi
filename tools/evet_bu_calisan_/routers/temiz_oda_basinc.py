from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.temiz_oda_basinc import TemizOdaBasinc, TemizOdaBasincCreate
from models.temiz_oda_basinc import TemizOdaBasinc as DBTemizOdaBasinc
from crud.temiz_oda_basinc import get_all_temiz_oda_basinc, get_temiz_oda_basinc_by_id, create_temiz_oda_basinc

router = APIRouter(prefix='/temiz_oda_basinc', tags=['TemizOdaBasinc'])

@router.get('/', response_model=list[TemizOdaBasinc])
async def list_temiz_oda_basinc(db: AsyncSession = Depends()):
    return await get_all_temiz_oda_basinc(db)

@router.get('/{id}', response_model=TemizOdaBasinc)
async def get_temiz_oda_basinc_item(id: int, db: AsyncSession = Depends()):
    result = await get_temiz_oda_basinc_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TemizOdaBasinc)
async def create_temiz_oda_basinc_item(data: TemizOdaBasincCreate, db: AsyncSession = Depends()):
    db_item = DBTemizOdaBasinc(**data.dict())
    return await create_temiz_oda_basinc(db, db_item)