from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_malzeme import ReceteMalzeme

async def get_all_recete_malzeme(db: AsyncSession):
    result = await db.execute(select(ReceteMalzeme))
    return result.scalars().all()

async def get_recete_malzeme_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteMalzeme).where(ReceteMalzeme.id == id))
    return result.scalar_one_or_none()

async def create_recete_malzeme(db: AsyncSession, obj: ReceteMalzeme):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj