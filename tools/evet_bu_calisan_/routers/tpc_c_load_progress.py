from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tpc_c_load_progress import TpcCLoadProgress, TpcCLoadProgressCreate
from models.tpc_c_load_progress import TpcCLoadProgress as DBTpcCLoadProgress
from crud.tpc_c_load_progress import get_all_tpc_c_load_progress, get_tpc_c_load_progress_by_id, create_tpc_c_load_progress

router = APIRouter(prefix='/tpc_c_load_progress', tags=['TpcCLoadProgress'])

@router.get('/', response_model=list[TpcCLoadProgress])
async def list_tpc_c_load_progress(db: AsyncSession = Depends()):
    return await get_all_tpc_c_load_progress(db)

@router.get('/{id}', response_model=TpcCLoadProgress)
async def get_tpc_c_load_progress_item(id: int, db: AsyncSession = Depends()):
    result = await get_tpc_c_load_progress_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TpcCLoadProgress)
async def create_tpc_c_load_progress_item(data: TpcCLoadProgressCreate, db: AsyncSession = Depends()):
    db_item = DBTpcCLoadProgress(**data.dict())
    return await create_tpc_c_load_progress(db, db_item)