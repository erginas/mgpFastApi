from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_detay import ReceteDetay

async def get_all_recete_detay(db: AsyncSession):
    result = await db.execute(select(ReceteDetay))
    return result.scalars().all()

async def get_recete_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteDetay).where(ReceteDetay.id == id))
    return result.scalar_one_or_none()

async def create_recete_detay(db: AsyncSession, obj: ReceteDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj