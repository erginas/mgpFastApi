from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_kutu import MalzemeKutu, MalzemeKutuCreate
from models.malzeme_kutu import MalzemeKutu as DBMalzemeKutu
from crud.malzeme_kutu import get_all_malzeme_kutu, get_malzeme_kutu_by_id, create_malzeme_kutu

router = APIRouter(prefix='/malzeme_kutu', tags=['MalzemeKutu'])

@router.get('/', response_model=list[MalzemeKutu])
async def list_malzeme_kutu(db: AsyncSession = Depends()):
    return await get_all_malzeme_kutu(db)

@router.get('/{id}', response_model=MalzemeKutu)
async def get_malzeme_kutu_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_kutu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeKutu)
async def create_malzeme_kutu_item(data: MalzemeKutuCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeKutu(**data.dict())
    return await create_malzeme_kutu(db, db_item)