from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_urun_agaci import ReceteUrunAgaci, ReceteUrunAgaciCreate
from models.recete_urun_agaci import ReceteUrunAgaci as DBReceteUrunAgaci
from crud.recete_urun_agaci import get_all_recete_urun_agaci, get_recete_urun_agaci_by_id, create_recete_urun_agaci

router = APIRouter(prefix='/recete_urun_agaci', tags=['ReceteUrunAgaci'])

@router.get('/', response_model=list[ReceteUrunAgaci])
async def list_recete_urun_agaci(db: AsyncSession = Depends()):
    return await get_all_recete_urun_agaci(db)

@router.get('/{id}', response_model=ReceteUrunAgaci)
async def get_recete_urun_agaci_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_urun_agaci_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteUrunAgaci)
async def create_recete_urun_agaci_item(data: ReceteUrunAgaciCreate, db: AsyncSession = Depends()):
    db_item = DBReceteUrunAgaci(**data.dict())
    return await create_recete_urun_agaci(db, db_item)