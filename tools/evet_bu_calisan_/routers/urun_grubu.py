from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.urun_grubu import UrunGrubu, UrunGrubuCreate
from models.urun_grubu import UrunGrubu as DBUrunGrubu
from crud.urun_grubu import get_all_urun_grubu, get_urun_grubu_by_id, create_urun_grubu

router = APIRouter(prefix='/urun_grubu', tags=['UrunGrubu'])

@router.get('/', response_model=list[UrunGrubu])
async def list_urun_grubu(db: AsyncSession = Depends()):
    return await get_all_urun_grubu(db)

@router.get('/{id}', response_model=UrunGrubu)
async def get_urun_grubu_item(id: int, db: AsyncSession = Depends()):
    result = await get_urun_grubu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UrunGrubu)
async def create_urun_grubu_item(data: UrunGrubuCreate, db: AsyncSession = Depends()):
    db_item = DBUrunGrubu(**data.dict())
    return await create_urun_grubu(db, db_item)