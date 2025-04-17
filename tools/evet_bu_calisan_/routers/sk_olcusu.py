from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sk_olcusu import SkOlcusu, SkOlcusuCreate
from models.sk_olcusu import SkOlcusu as DBSkOlcusu
from crud.sk_olcusu import get_all_sk_olcusu, get_sk_olcusu_by_id, create_sk_olcusu

router = APIRouter(prefix='/sk_olcusu', tags=['SkOlcusu'])

@router.get('/', response_model=list[SkOlcusu])
async def list_sk_olcusu(db: AsyncSession = Depends()):
    return await get_all_sk_olcusu(db)

@router.get('/{id}', response_model=SkOlcusu)
async def get_sk_olcusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_sk_olcusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SkOlcusu)
async def create_sk_olcusu_item(data: SkOlcusuCreate, db: AsyncSession = Depends()):
    db_item = DBSkOlcusu(**data.dict())
    return await create_sk_olcusu(db, db_item)