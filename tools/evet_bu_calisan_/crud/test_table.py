from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.test_table import TestTable

async def get_all_test_table(db: AsyncSession):
    result = await db.execute(select(TestTable))
    return result.scalars().all()

async def get_test_table_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TestTable).where(TestTable.id == id))
    return result.scalar_one_or_none()

async def create_test_table(db: AsyncSession, obj: TestTable):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj