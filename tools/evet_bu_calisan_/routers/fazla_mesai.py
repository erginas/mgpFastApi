from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.fazla_mesai import FazlaMesai, FazlaMesaiCreate
from models.fazla_mesai import FazlaMesai as DBFazlaMesai
from crud.fazla_mesai import get_all_fazla_mesai, get_fazla_mesai_by_id, create_fazla_mesai

router = APIRouter(prefix='/fazla_mesai', tags=['FazlaMesai'])

@router.get('/', response_model=list[FazlaMesai])
async def list_fazla_mesai(db: AsyncSession = Depends()):
    return await get_all_fazla_mesai(db)

@router.get('/{id}', response_model=FazlaMesai)
async def get_fazla_mesai_item(id: int, db: AsyncSession = Depends()):
    result = await get_fazla_mesai_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=FazlaMesai)
async def create_fazla_mesai_item(data: FazlaMesaiCreate, db: AsyncSession = Depends()):
    db_item = DBFazlaMesai(**data.dict())
    return await create_fazla_mesai(db, db_item)