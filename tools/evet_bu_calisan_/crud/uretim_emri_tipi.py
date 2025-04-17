from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uretim_emri_tipi import UretimEmriTipi

async def get_all_uretim_emri_tipi(db: AsyncSession):
    result = await db.execute(select(UretimEmriTipi))
    return result.scalars().all()

async def get_uretim_emri_tipi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UretimEmriTipi).where(UretimEmriTipi.id == id))
    return result.scalar_one_or_none()

async def create_uretim_emri_tipi(db: AsyncSession, obj: UretimEmriTipi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj