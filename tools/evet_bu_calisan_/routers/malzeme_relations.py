from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_relations import MalzemeRelations, MalzemeRelationsCreate
from models.malzeme_relations import MalzemeRelations as DBMalzemeRelations
from crud.malzeme_relations import get_all_malzeme_relations, get_malzeme_relations_by_id, create_malzeme_relations

router = APIRouter(prefix='/malzeme_relations', tags=['MalzemeRelations'])

@router.get('/', response_model=list[MalzemeRelations])
async def list_malzeme_relations(db: AsyncSession = Depends()):
    return await get_all_malzeme_relations(db)

@router.get('/{id}', response_model=MalzemeRelations)
async def get_malzeme_relations_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_relations_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeRelations)
async def create_malzeme_relations_item(data: MalzemeRelationsCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeRelations(**data.dict())
    return await create_malzeme_relations(db, db_item)