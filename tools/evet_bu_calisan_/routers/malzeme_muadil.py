from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_muadil import MalzemeMuadil, MalzemeMuadilCreate
from models.malzeme_muadil import MalzemeMuadil as DBMalzemeMuadil
from crud.malzeme_muadil import get_all_malzeme_muadil, get_malzeme_muadil_by_id, create_malzeme_muadil

router = APIRouter(prefix='/malzeme_muadil', tags=['MalzemeMuadil'])

@router.get('/', response_model=list[MalzemeMuadil])
async def list_malzeme_muadil(db: AsyncSession = Depends()):
    return await get_all_malzeme_muadil(db)

@router.get('/{id}', response_model=MalzemeMuadil)
async def get_malzeme_muadil_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_muadil_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeMuadil)
async def create_malzeme_muadil_item(data: MalzemeMuadilCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeMuadil(**data.dict())
    return await create_malzeme_muadil(db, db_item)