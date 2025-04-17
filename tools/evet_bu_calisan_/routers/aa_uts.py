from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aa_uts import AaUts, AaUtsCreate
from models.aa_uts import AaUts as DBAaUts
from crud.aa_uts import get_all_aa_uts, get_aa_uts_by_id, create_aa_uts

router = APIRouter(prefix='/aa_uts', tags=['AaUts'])

@router.get('/', response_model=list[AaUts])
async def list_aa_uts(db: AsyncSession = Depends()):
    return await get_all_aa_uts(db)

@router.get('/{id}', response_model=AaUts)
async def get_aa_uts_item(id: int, db: AsyncSession = Depends()):
    result = await get_aa_uts_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AaUts)
async def create_aa_uts_item(data: AaUtsCreate, db: AsyncSession = Depends()):
    db_item = DBAaUts(**data.dict())
    return await create_aa_uts(db, db_item)