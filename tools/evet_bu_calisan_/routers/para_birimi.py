from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.para_birimi import ParaBirimi, ParaBirimiCreate
from models.para_birimi import ParaBirimi as DBParaBirimi
from crud.para_birimi import get_all_para_birimi, get_para_birimi_by_id, create_para_birimi

router = APIRouter(prefix='/para_birimi', tags=['ParaBirimi'])

@router.get('/', response_model=list[ParaBirimi])
async def list_para_birimi(db: AsyncSession = Depends()):
    return await get_all_para_birimi(db)

@router.get('/{id}', response_model=ParaBirimi)
async def get_para_birimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_para_birimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ParaBirimi)
async def create_para_birimi_item(data: ParaBirimiCreate, db: AsyncSession = Depends()):
    db_item = DBParaBirimi(**data.dict())
    return await create_para_birimi(db, db_item)