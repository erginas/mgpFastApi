from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uretim_talep_detay import UretimTalepDetay

async def get_all_uretim_talep_detay(db: AsyncSession):
    result = await db.execute(select(UretimTalepDetay))
    return result.scalars().all()

async def get_uretim_talep_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UretimTalepDetay).where(UretimTalepDetay.id == id))
    return result.scalar_one_or_none()

async def create_uretim_talep_detay(db: AsyncSession, obj: UretimTalepDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj