from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.degerlendirme_kriteri import DegerlendirmeKriteri

async def get_all_degerlendirme_kriteri(db: AsyncSession):
    result = await db.execute(select(DegerlendirmeKriteri))
    return result.scalars().all()

async def get_degerlendirme_kriteri_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DegerlendirmeKriteri).where(DegerlendirmeKriteri.id == id))
    return result.scalar_one_or_none()

async def create_degerlendirme_kriteri(db: AsyncSession, obj: DegerlendirmeKriteri):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj