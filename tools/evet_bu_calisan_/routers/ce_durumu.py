from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ce_durumu import CeDurumu, CeDurumuCreate
from models.ce_durumu import CeDurumu as DBCeDurumu
from crud.ce_durumu import get_all_ce_durumu, get_ce_durumu_by_id, create_ce_durumu

router = APIRouter(prefix='/ce_durumu', tags=['CeDurumu'])

@router.get('/', response_model=list[CeDurumu])
async def list_ce_durumu(db: AsyncSession = Depends()):
    return await get_all_ce_durumu(db)

@router.get('/{id}', response_model=CeDurumu)
async def get_ce_durumu_item(id: int, db: AsyncSession = Depends()):
    result = await get_ce_durumu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=CeDurumu)
async def create_ce_durumu_item(data: CeDurumuCreate, db: AsyncSession = Depends()):
    db_item = DBCeDurumu(**data.dict())
    return await create_ce_durumu(db, db_item)