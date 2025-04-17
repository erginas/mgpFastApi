from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.degerlendirme_tablosu import DegerlendirmeTablosu

async def get_all_degerlendirme_tablosu(db: AsyncSession):
    result = await db.execute(select(DegerlendirmeTablosu))
    return result.scalars().all()

async def get_degerlendirme_tablosu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DegerlendirmeTablosu).where(DegerlendirmeTablosu.id == id))
    return result.scalar_one_or_none()

async def create_degerlendirme_tablosu(db: AsyncSession, obj: DegerlendirmeTablosu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj