from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_operasyonu import ReceteOperasyonu

async def get_all_recete_operasyonu(db: AsyncSession):
    result = await db.execute(select(ReceteOperasyonu))
    return result.scalars().all()

async def get_recete_operasyonu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteOperasyonu).where(ReceteOperasyonu.id == id))
    return result.scalar_one_or_none()

async def create_recete_operasyonu(db: AsyncSession, obj: ReceteOperasyonu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj