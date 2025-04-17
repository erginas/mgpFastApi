from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.firma import Firma, FirmaCreate
from models.firma import Firma as DBFirma
from crud.firma import get_all_firma, get_firma_by_id, create_firma

router = APIRouter(prefix='/firma', tags=['Firma'])

@router.get('/', response_model=list[Firma])
async def list_firma(db: AsyncSession = Depends()):
    return await get_all_firma(db)

@router.get('/{id}', response_model=Firma)
async def get_firma_item(id: int, db: AsyncSession = Depends()):
    result = await get_firma_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Firma)
async def create_firma_item(data: FirmaCreate, db: AsyncSession = Depends()):
    db_item = DBFirma(**data.dict())
    return await create_firma(db, db_item)