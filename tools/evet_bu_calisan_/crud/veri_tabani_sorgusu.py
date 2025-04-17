from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.veri_tabani_sorgusu import VeriTabaniSorgusu

async def get_all_veri_tabani_sorgusu(db: AsyncSession):
    result = await db.execute(select(VeriTabaniSorgusu))
    return result.scalars().all()

async def get_veri_tabani_sorgusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(VeriTabaniSorgusu).where(VeriTabaniSorgusu.id == id))
    return result.scalar_one_or_none()

async def create_veri_tabani_sorgusu(db: AsyncSession, obj: VeriTabaniSorgusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj