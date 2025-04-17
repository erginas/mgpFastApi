from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_tedarik_fiyati import MalzemeTedarikFiyati, MalzemeTedarikFiyatiCreate
from models.malzeme_tedarik_fiyati import MalzemeTedarikFiyati as DBMalzemeTedarikFiyati
from crud.malzeme_tedarik_fiyati import get_all_malzeme_tedarik_fiyati, get_malzeme_tedarik_fiyati_by_id, create_malzeme_tedarik_fiyati

router = APIRouter(prefix='/malzeme_tedarik_fiyati', tags=['MalzemeTedarikFiyati'])

@router.get('/', response_model=list[MalzemeTedarikFiyati])
async def list_malzeme_tedarik_fiyati(db: AsyncSession = Depends()):
    return await get_all_malzeme_tedarik_fiyati(db)

@router.get('/{id}', response_model=MalzemeTedarikFiyati)
async def get_malzeme_tedarik_fiyati_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_tedarik_fiyati_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeTedarikFiyati)
async def create_malzeme_tedarik_fiyati_item(data: MalzemeTedarikFiyatiCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeTedarikFiyati(**data.dict())
    return await create_malzeme_tedarik_fiyati(db, db_item)