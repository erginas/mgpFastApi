from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sayac_silinen import SayacSilinen

async def get_all_sayac_silinen(db: AsyncSession):
    result = await db.execute(select(SayacSilinen))
    return result.scalars().all()

async def get_sayac_silinen_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SayacSilinen).where(SayacSilinen.id == id))
    return result.scalar_one_or_none()

async def create_sayac_silinen(db: AsyncSession, obj: SayacSilinen):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj