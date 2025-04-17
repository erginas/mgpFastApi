from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ce_kapsam_2019 import CeKapsam2019, CeKapsam2019Create
from models.ce_kapsam_2019 import CeKapsam2019 as DBCeKapsam2019
from crud.ce_kapsam_2019 import get_all_ce_kapsam_2019, get_ce_kapsam_2019_by_id, create_ce_kapsam_2019

router = APIRouter(prefix='/ce_kapsam_2019', tags=['CeKapsam2019'])

@router.get('/', response_model=list[CeKapsam2019])
async def list_ce_kapsam_2019(db: AsyncSession = Depends()):
    return await get_all_ce_kapsam_2019(db)

@router.get('/{id}', response_model=CeKapsam2019)
async def get_ce_kapsam_2019_item(id: int, db: AsyncSession = Depends()):
    result = await get_ce_kapsam_2019_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=CeKapsam2019)
async def create_ce_kapsam_2019_item(data: CeKapsam2019Create, db: AsyncSession = Depends()):
    db_item = DBCeKapsam2019(**data.dict())
    return await create_ce_kapsam_2019(db, db_item)