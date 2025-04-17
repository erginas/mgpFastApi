from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_iliski import ReceteIliski

async def get_all_recete_iliski(db: AsyncSession):
    result = await db.execute(select(ReceteIliski))
    return result.scalars().all()

async def get_recete_iliski_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteIliski).where(ReceteIliski.id == id))
    return result.scalar_one_or_none()

async def create_recete_iliski(db: AsyncSession, obj: ReceteIliski):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj