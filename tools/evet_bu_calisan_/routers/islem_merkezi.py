from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.islem_merkezi import IslemMerkezi, IslemMerkeziCreate
from models.islem_merkezi import IslemMerkezi as DBIslemMerkezi
from crud.islem_merkezi import get_all_islem_merkezi, get_islem_merkezi_by_id, create_islem_merkezi

router = APIRouter(prefix='/islem_merkezi', tags=['IslemMerkezi'])

@router.get('/', response_model=list[IslemMerkezi])
async def list_islem_merkezi(db: AsyncSession = Depends()):
    return await get_all_islem_merkezi(db)

@router.get('/{id}', response_model=IslemMerkezi)
async def get_islem_merkezi_item(id: int, db: AsyncSession = Depends()):
    result = await get_islem_merkezi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IslemMerkezi)
async def create_islem_merkezi_item(data: IslemMerkeziCreate, db: AsyncSession = Depends()):
    db_item = DBIslemMerkezi(**data.dict())
    return await create_islem_merkezi(db, db_item)