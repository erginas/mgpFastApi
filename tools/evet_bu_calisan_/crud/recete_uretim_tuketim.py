from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_uretim_tuketim import ReceteUretimTuketim

async def get_all_recete_uretim_tuketim(db: AsyncSession):
    result = await db.execute(select(ReceteUretimTuketim))
    return result.scalars().all()

async def get_recete_uretim_tuketim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteUretimTuketim).where(ReceteUretimTuketim.id == id))
    return result.scalar_one_or_none()

async def create_recete_uretim_tuketim(db: AsyncSession, obj: ReceteUretimTuketim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj