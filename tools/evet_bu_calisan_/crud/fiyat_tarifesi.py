from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.fiyat_tarifesi import FiyatTarifesi

async def get_all_fiyat_tarifesi(db: AsyncSession):
    result = await db.execute(select(FiyatTarifesi))
    return result.scalars().all()

async def get_fiyat_tarifesi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FiyatTarifesi).where(FiyatTarifesi.id == id))
    return result.scalar_one_or_none()

async def create_fiyat_tarifesi(db: AsyncSession, obj: FiyatTarifesi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj