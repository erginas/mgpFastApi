from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tezgah import Tezgah

async def get_all_tezgah(db: AsyncSession):
    result = await db.execute(select(Tezgah))
    return result.scalars().all()

async def get_tezgah_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Tezgah).where(Tezgah.id == id))
    return result.scalar_one_or_none()

async def create_tezgah(db: AsyncSession, obj: Tezgah):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj