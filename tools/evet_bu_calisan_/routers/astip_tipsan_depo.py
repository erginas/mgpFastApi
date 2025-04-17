from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.astip_tipsan_depo import AstipTipsanDepo, AstipTipsanDepoCreate
from models.astip_tipsan_depo import AstipTipsanDepo as DBAstipTipsanDepo
from crud.astip_tipsan_depo import get_all_astip_tipsan_depo, get_astip_tipsan_depo_by_id, create_astip_tipsan_depo

router = APIRouter(prefix='/astip_tipsan_depo', tags=['AstipTipsanDepo'])

@router.get('/', response_model=list[AstipTipsanDepo])
async def list_astip_tipsan_depo(db: AsyncSession = Depends()):
    return await get_all_astip_tipsan_depo(db)

@router.get('/{id}', response_model=AstipTipsanDepo)
async def get_astip_tipsan_depo_item(id: int, db: AsyncSession = Depends()):
    result = await get_astip_tipsan_depo_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AstipTipsanDepo)
async def create_astip_tipsan_depo_item(data: AstipTipsanDepoCreate, db: AsyncSession = Depends()):
    db_item = DBAstipTipsanDepo(**data.dict())
    return await create_astip_tipsan_depo(db, db_item)