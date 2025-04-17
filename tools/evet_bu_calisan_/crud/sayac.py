from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sayac import Sayac

async def get_all_sayac(db: AsyncSession):
    result = await db.execute(select(Sayac))
    return result.scalars().all()

async def get_sayac_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Sayac).where(Sayac.id == id))
    return result.scalar_one_or_none()

async def create_sayac(db: AsyncSession, obj: Sayac):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj