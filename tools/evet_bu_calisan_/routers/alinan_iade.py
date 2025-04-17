from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_iade import AlinanIade, AlinanIadeCreate
from models.alinan_iade import AlinanIade as DBAlinanIade
from crud.alinan_iade import get_all_alinan_iade, get_alinan_iade_by_id, create_alinan_iade

router = APIRouter(prefix='/alinan_iade', tags=['AlinanIade'])

@router.get('/', response_model=list[AlinanIade])
async def list_alinan_iade(db: AsyncSession = Depends()):
    return await get_all_alinan_iade(db)

@router.get('/{id}', response_model=AlinanIade)
async def get_alinan_iade_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_iade_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanIade)
async def create_alinan_iade_item(data: AlinanIadeCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanIade(**data.dict())
    return await create_alinan_iade(db, db_item)