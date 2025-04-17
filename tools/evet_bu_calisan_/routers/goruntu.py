from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.goruntu import Goruntu, GoruntuCreate
from models.goruntu import Goruntu as DBGoruntu
from crud.goruntu import get_all_goruntu, get_goruntu_by_id, create_goruntu

router = APIRouter(prefix='/goruntu', tags=['Goruntu'])

@router.get('/', response_model=list[Goruntu])
async def list_goruntu(db: AsyncSession = Depends()):
    return await get_all_goruntu(db)

@router.get('/{id}', response_model=Goruntu)
async def get_goruntu_item(id: int, db: AsyncSession = Depends()):
    result = await get_goruntu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Goruntu)
async def create_goruntu_item(data: GoruntuCreate, db: AsyncSession = Depends()):
    db_item = DBGoruntu(**data.dict())
    return await create_goruntu(db, db_item)