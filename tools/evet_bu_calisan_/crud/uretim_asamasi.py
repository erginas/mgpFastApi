from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uretim_asamasi import UretimAsamasi

async def get_all_uretim_asamasi(db: AsyncSession):
    result = await db.execute(select(UretimAsamasi))
    return result.scalars().all()

async def get_uretim_asamasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UretimAsamasi).where(UretimAsamasi.id == id))
    return result.scalar_one_or_none()

async def create_uretim_asamasi(db: AsyncSession, obj: UretimAsamasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj