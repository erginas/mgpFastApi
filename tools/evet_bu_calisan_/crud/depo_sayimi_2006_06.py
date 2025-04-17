from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2006_06 import DepoSayimi200606

async def get_all_depo_sayimi_2006_06(db: AsyncSession):
    result = await db.execute(select(DepoSayimi200606))
    return result.scalars().all()

async def get_depo_sayimi_2006_06_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi200606).where(DepoSayimi200606.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2006_06(db: AsyncSession, obj: DepoSayimi200606):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj