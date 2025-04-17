from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.chained_rows import ChainedRows, ChainedRowsCreate
from models.chained_rows import ChainedRows as DBChainedRows
from crud.chained_rows import get_all_chained_rows, get_chained_rows_by_id, create_chained_rows

router = APIRouter(prefix='/chained_rows', tags=['ChainedRows'])

@router.get('/', response_model=list[ChainedRows])
async def list_chained_rows(db: AsyncSession = Depends()):
    return await get_all_chained_rows(db)

@router.get('/{id}', response_model=ChainedRows)
async def get_chained_rows_item(id: int, db: AsyncSession = Depends()):
    result = await get_chained_rows_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ChainedRows)
async def create_chained_rows_item(data: ChainedRowsCreate, db: AsyncSession = Depends()):
    db_item = DBChainedRows(**data.dict())
    return await create_chained_rows(db, db_item)