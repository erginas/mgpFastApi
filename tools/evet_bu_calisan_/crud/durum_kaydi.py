from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.durum_kaydi import DurumKaydi

async def get_all_durum_kaydi(db: AsyncSession):
    result = await db.execute(select(DurumKaydi))
    return result.scalars().all()

async def get_durum_kaydi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DurumKaydi).where(DurumKaydi.id == id))
    return result.scalar_one_or_none()

async def create_durum_kaydi(db: AsyncSession, obj: DurumKaydi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj