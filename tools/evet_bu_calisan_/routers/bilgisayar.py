from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.bilgisayar import Bilgisayar, BilgisayarCreate
from models.bilgisayar import Bilgisayar as DBBilgisayar
from crud.bilgisayar import get_all_bilgisayar, get_bilgisayar_by_id, create_bilgisayar

router = APIRouter(prefix='/bilgisayar', tags=['Bilgisayar'])

@router.get('/', response_model=list[Bilgisayar])
async def list_bilgisayar(db: AsyncSession = Depends()):
    return await get_all_bilgisayar(db)

@router.get('/{id}', response_model=Bilgisayar)
async def get_bilgisayar_item(id: int, db: AsyncSession = Depends()):
    result = await get_bilgisayar_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Bilgisayar)
async def create_bilgisayar_item(data: BilgisayarCreate, db: AsyncSession = Depends()):
    db_item = DBBilgisayar(**data.dict())
    return await create_bilgisayar(db, db_item)