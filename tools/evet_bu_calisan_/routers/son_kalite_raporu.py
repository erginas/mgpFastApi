from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.son_kalite_raporu import SonKaliteRaporu, SonKaliteRaporuCreate
from models.son_kalite_raporu import SonKaliteRaporu as DBSonKaliteRaporu
from crud.son_kalite_raporu import get_all_son_kalite_raporu, get_son_kalite_raporu_by_id, create_son_kalite_raporu

router = APIRouter(prefix='/son_kalite_raporu', tags=['SonKaliteRaporu'])

@router.get('/', response_model=list[SonKaliteRaporu])
async def list_son_kalite_raporu(db: AsyncSession = Depends()):
    return await get_all_son_kalite_raporu(db)

@router.get('/{id}', response_model=SonKaliteRaporu)
async def get_son_kalite_raporu_item(id: int, db: AsyncSession = Depends()):
    result = await get_son_kalite_raporu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SonKaliteRaporu)
async def create_son_kalite_raporu_item(data: SonKaliteRaporuCreate, db: AsyncSession = Depends()):
    db_item = DBSonKaliteRaporu(**data.dict())
    return await create_son_kalite_raporu(db, db_item)