from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2015_0211_ma import DepoSayimi20150211Ma

async def get_all_depo_sayimi_2015_0211_ma(db: AsyncSession):
    result = await db.execute(select(DepoSayimi20150211Ma))
    return result.scalars().all()

async def get_depo_sayimi_2015_0211_ma_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi20150211Ma).where(DepoSayimi20150211Ma.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2015_0211_ma(db: AsyncSession, obj: DepoSayimi20150211Ma):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj