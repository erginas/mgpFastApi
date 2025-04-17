from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.parametre import Parametre, ParametreCreate
from models.parametre import Parametre as DBParametre
from crud.parametre import get_all_parametre, get_parametre_by_id, create_parametre

router = APIRouter(prefix='/parametre', tags=['Parametre'])

@router.get('/', response_model=list[Parametre])
async def list_parametre(db: AsyncSession = Depends()):
    return await get_all_parametre(db)

@router.get('/{id}', response_model=Parametre)
async def get_parametre_item(id: int, db: AsyncSession = Depends()):
    result = await get_parametre_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Parametre)
async def create_parametre_item(data: ParametreCreate, db: AsyncSession = Depends()):
    db_item = DBParametre(**data.dict())
    return await create_parametre(db, db_item)