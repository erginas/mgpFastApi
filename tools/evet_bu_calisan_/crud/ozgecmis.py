from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ozgecmis import Ozgecmis

async def get_all_ozgecmis(db: AsyncSession):
    result = await db.execute(select(Ozgecmis))
    return result.scalars().all()

async def get_ozgecmis_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Ozgecmis).where(Ozgecmis.id == id))
    return result.scalar_one_or_none()

async def create_ozgecmis(db: AsyncSession, obj: Ozgecmis):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj