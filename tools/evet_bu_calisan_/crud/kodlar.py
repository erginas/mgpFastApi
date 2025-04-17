from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kodlar import Kodlar

async def get_all_kodlar(db: AsyncSession):
    result = await db.execute(select(Kodlar))
    return result.scalars().all()

async def get_kodlar_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Kodlar).where(Kodlar.id == id))
    return result.scalar_one_or_none()

async def create_kodlar(db: AsyncSession, obj: Kodlar):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj