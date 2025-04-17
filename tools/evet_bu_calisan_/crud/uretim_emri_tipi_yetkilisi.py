from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uretim_emri_tipi_yetkilisi import UretimEmriTipiYetkilisi

async def get_all_uretim_emri_tipi_yetkilisi(db: AsyncSession):
    result = await db.execute(select(UretimEmriTipiYetkilisi))
    return result.scalars().all()

async def get_uretim_emri_tipi_yetkilisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UretimEmriTipiYetkilisi).where(UretimEmriTipiYetkilisi.id == id))
    return result.scalar_one_or_none()

async def create_uretim_emri_tipi_yetkilisi(db: AsyncSession, obj: UretimEmriTipiYetkilisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj