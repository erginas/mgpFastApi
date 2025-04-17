from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kisi_rolu import KisiRolu, KisiRoluCreate
from models.kisi_rolu import KisiRolu as DBKisiRolu
from crud.kisi_rolu import get_all_kisi_rolu, get_kisi_rolu_by_id, create_kisi_rolu

router = APIRouter(prefix='/kisi_rolu', tags=['KisiRolu'])

@router.get('/', response_model=list[KisiRolu])
async def list_kisi_rolu(db: AsyncSession = Depends()):
    return await get_all_kisi_rolu(db)

@router.get('/{id}', response_model=KisiRolu)
async def get_kisi_rolu_item(id: int, db: AsyncSession = Depends()):
    result = await get_kisi_rolu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KisiRolu)
async def create_kisi_rolu_item(data: KisiRoluCreate, db: AsyncSession = Depends()):
    db_item = DBKisiRolu(**data.dict())
    return await create_kisi_rolu(db, db_item)