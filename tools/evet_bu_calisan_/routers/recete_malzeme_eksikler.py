from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_malzeme_eksikler import ReceteMalzemeEksikler, ReceteMalzemeEksiklerCreate
from models.recete_malzeme_eksikler import ReceteMalzemeEksikler as DBReceteMalzemeEksikler
from crud.recete_malzeme_eksikler import get_all_recete_malzeme_eksikler, get_recete_malzeme_eksikler_by_id, create_recete_malzeme_eksikler

router = APIRouter(prefix='/recete_malzeme_eksikler', tags=['ReceteMalzemeEksikler'])

@router.get('/', response_model=list[ReceteMalzemeEksikler])
async def list_recete_malzeme_eksikler(db: AsyncSession = Depends()):
    return await get_all_recete_malzeme_eksikler(db)

@router.get('/{id}', response_model=ReceteMalzemeEksikler)
async def get_recete_malzeme_eksikler_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_malzeme_eksikler_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteMalzemeEksikler)
async def create_recete_malzeme_eksikler_item(data: ReceteMalzemeEksiklerCreate, db: AsyncSession = Depends()):
    db_item = DBReceteMalzemeEksikler(**data.dict())
    return await create_recete_malzeme_eksikler(db, db_item)