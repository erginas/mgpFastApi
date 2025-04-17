from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.banka import Banka

async def get_all_banka(db: AsyncSession):
    result = await db.execute(select(Banka))
    return result.scalars().all()

async def get_banka_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Banka).where(Banka.id == id))
    return result.scalar_one_or_none()

async def create_banka(db: AsyncSession, obj: Banka):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj