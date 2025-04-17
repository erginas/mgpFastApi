from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.modul import Modul, ModulCreate
from models.modul import Modul as DBModul
from crud.modul import get_all_modul, get_modul_by_id, create_modul

router = APIRouter(prefix='/modul', tags=['Modul'])

@router.get('/', response_model=list[Modul])
async def list_modul(db: AsyncSession = Depends()):
    return await get_all_modul(db)

@router.get('/{id}', response_model=Modul)
async def get_modul_item(id: int, db: AsyncSession = Depends()):
    result = await get_modul_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Modul)
async def create_modul_item(data: ModulCreate, db: AsyncSession = Depends()):
    db_item = DBModul(**data.dict())
    return await create_modul(db, db_item)