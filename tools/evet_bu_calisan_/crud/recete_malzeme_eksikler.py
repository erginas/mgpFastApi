from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_malzeme_eksikler import ReceteMalzemeEksikler

async def get_all_recete_malzeme_eksikler(db: AsyncSession):
    result = await db.execute(select(ReceteMalzemeEksikler))
    return result.scalars().all()

async def get_recete_malzeme_eksikler_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteMalzemeEksikler).where(ReceteMalzemeEksikler.id == id))
    return result.scalar_one_or_none()

async def create_recete_malzeme_eksikler(db: AsyncSession, obj: ReceteMalzemeEksikler):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj