from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_alt_detay import ReceteAltDetay

async def get_all_recete_alt_detay(db: AsyncSession):
    result = await db.execute(select(ReceteAltDetay))
    return result.scalars().all()

async def get_recete_alt_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteAltDetay).where(ReceteAltDetay.id == id))
    return result.scalar_one_or_none()

async def create_recete_alt_detay(db: AsyncSession, obj: ReceteAltDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj