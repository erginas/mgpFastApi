from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tpc_c_block_info import TpcCBlockInfo, TpcCBlockInfoCreate
from models.tpc_c_block_info import TpcCBlockInfo as DBTpcCBlockInfo
from crud.tpc_c_block_info import get_all_tpc_c_block_info, get_tpc_c_block_info_by_id, create_tpc_c_block_info

router = APIRouter(prefix='/tpc_c_block_info', tags=['TpcCBlockInfo'])

@router.get('/', response_model=list[TpcCBlockInfo])
async def list_tpc_c_block_info(db: AsyncSession = Depends()):
    return await get_all_tpc_c_block_info(db)

@router.get('/{id}', response_model=TpcCBlockInfo)
async def get_tpc_c_block_info_item(id: int, db: AsyncSession = Depends()):
    result = await get_tpc_c_block_info_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TpcCBlockInfo)
async def create_tpc_c_block_info_item(data: TpcCBlockInfoCreate, db: AsyncSession = Depends()):
    db_item = DBTpcCBlockInfo(**data.dict())
    return await create_tpc_c_block_info(db, db_item)