from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygulama_menusu import UygulamaMenusu, UygulamaMenusuCreate
from models.uygulama_menusu import UygulamaMenusu as DBUygulamaMenusu
from crud.uygulama_menusu import get_all_uygulama_menusu, get_uygulama_menusu_by_id, create_uygulama_menusu

router = APIRouter(prefix='/uygulama_menusu', tags=['UygulamaMenusu'])

@router.get('/', response_model=list[UygulamaMenusu])
async def list_uygulama_menusu(db: AsyncSession = Depends()):
    return await get_all_uygulama_menusu(db)

@router.get('/{id}', response_model=UygulamaMenusu)
async def get_uygulama_menusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygulama_menusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygulamaMenusu)
async def create_uygulama_menusu_item(data: UygulamaMenusuCreate, db: AsyncSession = Depends()):
    db_item = DBUygulamaMenusu(**data.dict())
    return await create_uygulama_menusu(db, db_item)