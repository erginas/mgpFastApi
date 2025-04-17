from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.firma_degerlendirmesi import FirmaDegerlendirmesi

async def get_all_firma_degerlendirmesi(db: AsyncSession):
    result = await db.execute(select(FirmaDegerlendirmesi))
    return result.scalars().all()

async def get_firma_degerlendirmesi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FirmaDegerlendirmesi).where(FirmaDegerlendirmesi.id == id))
    return result.scalar_one_or_none()

async def create_firma_degerlendirmesi(db: AsyncSession, obj: FirmaDegerlendirmesi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj