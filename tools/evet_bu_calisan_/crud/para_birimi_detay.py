from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.para_birimi_detay import ParaBirimiDetay

async def get_all_para_birimi_detay(db: AsyncSession):
    result = await db.execute(select(ParaBirimiDetay))
    return result.scalars().all()

async def get_para_birimi_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ParaBirimiDetay).where(ParaBirimiDetay.id == id))
    return result.scalar_one_or_none()

async def create_para_birimi_detay(db: AsyncSession, obj: ParaBirimiDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj