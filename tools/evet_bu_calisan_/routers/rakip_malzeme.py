from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.rakip_malzeme import RakipMalzeme, RakipMalzemeCreate
from models.rakip_malzeme import RakipMalzeme as DBRakipMalzeme
from crud.rakip_malzeme import get_all_rakip_malzeme, get_rakip_malzeme_by_id, create_rakip_malzeme

router = APIRouter(prefix='/rakip_malzeme', tags=['RakipMalzeme'])

@router.get('/', response_model=list[RakipMalzeme])
async def list_rakip_malzeme(db: AsyncSession = Depends()):
    return await get_all_rakip_malzeme(db)

@router.get('/{id}', response_model=RakipMalzeme)
async def get_rakip_malzeme_item(id: int, db: AsyncSession = Depends()):
    result = await get_rakip_malzeme_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=RakipMalzeme)
async def create_rakip_malzeme_item(data: RakipMalzemeCreate, db: AsyncSession = Depends()):
    db_item = DBRakipMalzeme(**data.dict())
    return await create_rakip_malzeme(db, db_item)