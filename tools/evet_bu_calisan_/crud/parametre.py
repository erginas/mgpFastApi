from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.parametre import Parametre

async def get_all_parametre(db: AsyncSession):
    result = await db.execute(select(Parametre))
    return result.scalars().all()

async def get_parametre_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Parametre).where(Parametre.id == id))
    return result.scalar_one_or_none()

async def create_parametre(db: AsyncSession, obj: Parametre):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj