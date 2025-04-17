from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aktarma import Aktarma

async def get_all_aktarma(db: AsyncSession):
    result = await db.execute(select(Aktarma))
    return result.scalars().all()

async def get_aktarma_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Aktarma).where(Aktarma.id == id))
    return result.scalar_one_or_none()

async def create_aktarma(db: AsyncSession, obj: Aktarma):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj