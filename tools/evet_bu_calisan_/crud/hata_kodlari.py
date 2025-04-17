from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.hata_kodlari import HataKodlari

async def get_all_hata_kodlari(db: AsyncSession):
    result = await db.execute(select(HataKodlari))
    return result.scalars().all()

async def get_hata_kodlari_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HataKodlari).where(HataKodlari.id == id))
    return result.scalar_one_or_none()

async def create_hata_kodlari(db: AsyncSession, obj: HataKodlari):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj