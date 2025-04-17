from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.temiz_oda_basinc import TemizOdaBasinc

async def get_all_temiz_oda_basinc(db: AsyncSession):
    result = await db.execute(select(TemizOdaBasinc))
    return result.scalars().all()

async def get_temiz_oda_basinc_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TemizOdaBasinc).where(TemizOdaBasinc.id == id))
    return result.scalar_one_or_none()

async def create_temiz_oda_basinc(db: AsyncSession, obj: TemizOdaBasinc):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj