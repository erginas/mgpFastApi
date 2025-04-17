from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sistem_rolu_formu import SistemRoluFormu

async def get_all_sistem_rolu_formu(db: AsyncSession):
    result = await db.execute(select(SistemRoluFormu))
    return result.scalars().all()

async def get_sistem_rolu_formu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SistemRoluFormu).where(SistemRoluFormu.id == id))
    return result.scalar_one_or_none()

async def create_sistem_rolu_formu(db: AsyncSession, obj: SistemRoluFormu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj