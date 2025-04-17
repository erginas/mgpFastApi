from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_uretim_asamasi import ReceteUretimAsamasi

async def get_all_recete_uretim_asamasi(db: AsyncSession):
    result = await db.execute(select(ReceteUretimAsamasi))
    return result.scalars().all()

async def get_recete_uretim_asamasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteUretimAsamasi).where(ReceteUretimAsamasi.id == id))
    return result.scalar_one_or_none()

async def create_recete_uretim_asamasi(db: AsyncSession, obj: ReceteUretimAsamasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj