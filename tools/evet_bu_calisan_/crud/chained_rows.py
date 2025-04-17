from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.chained_rows import ChainedRows

async def get_all_chained_rows(db: AsyncSession):
    result = await db.execute(select(ChainedRows))
    return result.scalars().all()

async def get_chained_rows_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ChainedRows).where(ChainedRows.id == id))
    return result.scalar_one_or_none()

async def create_chained_rows(db: AsyncSession, obj: ChainedRows):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj