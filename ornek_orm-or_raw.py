from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from core.dependencies import get_session, execute_raw_sql

router = APIRouter()

@router.get("/raw-sorgu")
async def calistir():
    query = "SELECT * FROM IS_EMRI_OPERASYONU WHERE ROWNUM < 10"
    return await execute_raw_sql(query)

@router.get("/orm-kullan")
async def orm_ornegi(session: AsyncSession = Depends(get_session)):
    result = await session.execute(text("SELECT * FROM IS_EMRI_OPERASYONU WHERE ROWNUM < 5"))
    return [dict(row._mapping) for row in result]