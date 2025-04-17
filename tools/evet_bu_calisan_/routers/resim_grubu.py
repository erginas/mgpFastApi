from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.resim_grubu import ResimGrubu, ResimGrubuCreate
from models.resim_grubu import ResimGrubu as DBResimGrubu
from crud.resim_grubu import get_all_resim_grubu, get_resim_grubu_by_id, create_resim_grubu

router = APIRouter(prefix='/resim_grubu', tags=['ResimGrubu'])

@router.get('/', response_model=list[ResimGrubu])
async def list_resim_grubu(db: AsyncSession = Depends()):
    return await get_all_resim_grubu(db)

@router.get('/{id}', response_model=ResimGrubu)
async def get_resim_grubu_item(id: int, db: AsyncSession = Depends()):
    result = await get_resim_grubu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ResimGrubu)
async def create_resim_grubu_item(data: ResimGrubuCreate, db: AsyncSession = Depends()):
    db_item = DBResimGrubu(**data.dict())
    return await create_resim_grubu(db, db_item)