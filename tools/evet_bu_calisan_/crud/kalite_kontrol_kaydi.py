from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kalite_kontrol_kaydi import KaliteKontrolKaydi

async def get_all_kalite_kontrol_kaydi(db: AsyncSession):
    result = await db.execute(select(KaliteKontrolKaydi))
    return result.scalars().all()

async def get_kalite_kontrol_kaydi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KaliteKontrolKaydi).where(KaliteKontrolKaydi.id == id))
    return result.scalar_one_or_none()

async def create_kalite_kontrol_kaydi(db: AsyncSession, obj: KaliteKontrolKaydi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj