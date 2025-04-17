from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_ozelligi import ReceteOzelligi

async def get_all_recete_ozelligi(db: AsyncSession):
    result = await db.execute(select(ReceteOzelligi))
    return result.scalars().all()

async def get_recete_ozelligi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteOzelligi).where(ReceteOzelligi.id == id))
    return result.scalar_one_or_none()

async def create_recete_ozelligi(db: AsyncSession, obj: ReceteOzelligi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj