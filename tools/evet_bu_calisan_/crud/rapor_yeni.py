from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.rapor_yeni import RaporYeni

async def get_all_rapor_yeni(db: AsyncSession):
    result = await db.execute(select(RaporYeni))
    return result.scalars().all()

async def get_rapor_yeni_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(RaporYeni).where(RaporYeni.id == id))
    return result.scalar_one_or_none()

async def create_rapor_yeni(db: AsyncSession, obj: RaporYeni):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj