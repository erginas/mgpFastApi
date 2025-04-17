from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_grubu import MalzemeGrubu, MalzemeGrubuCreate
from models.malzeme_grubu import MalzemeGrubu as DBMalzemeGrubu
from crud.malzeme_grubu import get_all_malzeme_grubu, get_malzeme_grubu_by_id, create_malzeme_grubu

router = APIRouter(prefix='/malzeme_grubu', tags=['MalzemeGrubu'])

@router.get('/', response_model=list[MalzemeGrubu])
async def list_malzeme_grubu(db: AsyncSession = Depends()):
    return await get_all_malzeme_grubu(db)

@router.get('/{id}', response_model=MalzemeGrubu)
async def get_malzeme_grubu_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_grubu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeGrubu)
async def create_malzeme_grubu_item(data: MalzemeGrubuCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeGrubu(**data.dict())
    return await create_malzeme_grubu(db, db_item)