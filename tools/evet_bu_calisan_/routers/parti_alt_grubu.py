from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.parti_alt_grubu import PartiAltGrubu, PartiAltGrubuCreate
from models.parti_alt_grubu import PartiAltGrubu as DBPartiAltGrubu
from crud.parti_alt_grubu import get_all_parti_alt_grubu, get_parti_alt_grubu_by_id, create_parti_alt_grubu

router = APIRouter(prefix='/parti_alt_grubu', tags=['PartiAltGrubu'])

@router.get('/', response_model=list[PartiAltGrubu])
async def list_parti_alt_grubu(db: AsyncSession = Depends()):
    return await get_all_parti_alt_grubu(db)

@router.get('/{id}', response_model=PartiAltGrubu)
async def get_parti_alt_grubu_item(id: int, db: AsyncSession = Depends()):
    result = await get_parti_alt_grubu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=PartiAltGrubu)
async def create_parti_alt_grubu_item(data: PartiAltGrubuCreate, db: AsyncSession = Depends()):
    db_item = DBPartiAltGrubu(**data.dict())
    return await create_parti_alt_grubu(db, db_item)