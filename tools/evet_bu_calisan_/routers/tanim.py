from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tanim import Tanim, TanimCreate
from models.tanim import Tanim as DBTanim
from crud.tanim import get_all_tanim, get_tanim_by_id, create_tanim

router = APIRouter(prefix='/tanim', tags=['Tanim'])

@router.get('/', response_model=list[Tanim])
async def list_tanim(db: AsyncSession = Depends()):
    return await get_all_tanim(db)

@router.get('/{id}', response_model=Tanim)
async def get_tanim_item(id: int, db: AsyncSession = Depends()):
    result = await get_tanim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Tanim)
async def create_tanim_item(data: TanimCreate, db: AsyncSession = Depends()):
    db_item = DBTanim(**data.dict())
    return await create_tanim(db, db_item)