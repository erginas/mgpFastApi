from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.temin_sekli import TeminSekli

async def get_all_temin_sekli(db: AsyncSession):
    result = await db.execute(select(TeminSekli))
    return result.scalars().all()

async def get_temin_sekli_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TeminSekli).where(TeminSekli.id == id))
    return result.scalar_one_or_none()

async def create_temin_sekli(db: AsyncSession, obj: TeminSekli):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj