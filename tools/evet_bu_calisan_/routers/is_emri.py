from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri import IsEmri, IsEmriCreate
from models.is_emri import IsEmri as DBIsEmri
from crud.is_emri import get_all_is_emri, get_is_emri_by_id, create_is_emri

router = APIRouter(prefix='/is_emri', tags=['IsEmri'])

@router.get('/', response_model=list[IsEmri])
async def list_is_emri(db: AsyncSession = Depends()):
    return await get_all_is_emri(db)

@router.get('/{id}', response_model=IsEmri)
async def get_is_emri_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmri)
async def create_is_emri_item(data: IsEmriCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmri(**data.dict())
    return await create_is_emri(db, db_item)