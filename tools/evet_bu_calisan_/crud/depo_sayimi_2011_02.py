from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2011_02 import DepoSayimi201102

async def get_all_depo_sayimi_2011_02(db: AsyncSession):
    result = await db.execute(select(DepoSayimi201102))
    return result.scalars().all()

async def get_depo_sayimi_2011_02_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi201102).where(DepoSayimi201102.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2011_02(db: AsyncSession, obj: DepoSayimi201102):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj