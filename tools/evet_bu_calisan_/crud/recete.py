from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete import Recete

async def get_all_recete(db: AsyncSession):
    result = await db.execute(select(Recete))
    return result.scalars().all()

async def get_recete_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Recete).where(Recete.id == id))
    return result.scalar_one_or_none()

async def create_recete(db: AsyncSession, obj: Recete):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj