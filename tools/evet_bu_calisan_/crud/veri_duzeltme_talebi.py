from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.veri_duzeltme_talebi import VeriDuzeltmeTalebi

async def get_all_veri_duzeltme_talebi(db: AsyncSession):
    result = await db.execute(select(VeriDuzeltmeTalebi))
    return result.scalars().all()

async def get_veri_duzeltme_talebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(VeriDuzeltmeTalebi).where(VeriDuzeltmeTalebi.id == id))
    return result.scalar_one_or_none()

async def create_veri_duzeltme_talebi(db: AsyncSession, obj: VeriDuzeltmeTalebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj