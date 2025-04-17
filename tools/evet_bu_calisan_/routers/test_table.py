from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.test_table import TestTable, TestTableCreate
from models.test_table import TestTable as DBTestTable
from crud.test_table import get_all_test_table, get_test_table_by_id, create_test_table

router = APIRouter(prefix='/test_table', tags=['TestTable'])

@router.get('/', response_model=list[TestTable])
async def list_test_table(db: AsyncSession = Depends()):
    return await get_all_test_table(db)

@router.get('/{id}', response_model=TestTable)
async def get_test_table_item(id: int, db: AsyncSession = Depends()):
    result = await get_test_table_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TestTable)
async def create_test_table_item(data: TestTableCreate, db: AsyncSession = Depends()):
    db_item = DBTestTable(**data.dict())
    return await create_test_table(db, db_item)