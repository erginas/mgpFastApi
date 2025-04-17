from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.astip_depo import AstipDepo, AstipDepoCreate
from models.astip_depo import AstipDepo as DBAstipDepo
from crud.astip_depo import get_all_astip_depo, get_astip_depo_by_id, create_astip_depo

router = APIRouter(prefix='/astip_depo', tags=['AstipDepo'])

@router.get('/', response_model=list[AstipDepo])
async def list_astip_depo(db: AsyncSession = Depends()):
    return await get_all_astip_depo(db)

@router.get('/{id}', response_model=AstipDepo)
async def get_astip_depo_item(id: int, db: AsyncSession = Depends()):
    result = await get_astip_depo_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AstipDepo)
async def create_astip_depo_item(data: AstipDepoCreate, db: AsyncSession = Depends()):
    db_item = DBAstipDepo(**data.dict())
    return await create_astip_depo(db, db_item)