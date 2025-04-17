from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ozgecmis import Ozgecmis, OzgecmisCreate
from models.ozgecmis import Ozgecmis as DBOzgecmis
from crud.ozgecmis import get_all_ozgecmis, get_ozgecmis_by_id, create_ozgecmis

router = APIRouter(prefix='/ozgecmis', tags=['Ozgecmis'])

@router.get('/', response_model=list[Ozgecmis])
async def list_ozgecmis(db: AsyncSession = Depends()):
    return await get_all_ozgecmis(db)

@router.get('/{id}', response_model=Ozgecmis)
async def get_ozgecmis_item(id: int, db: AsyncSession = Depends()):
    result = await get_ozgecmis_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Ozgecmis)
async def create_ozgecmis_item(data: OzgecmisCreate, db: AsyncSession = Depends()):
    db_item = DBOzgecmis(**data.dict())
    return await create_ozgecmis(db, db_item)