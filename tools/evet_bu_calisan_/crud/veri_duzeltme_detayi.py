from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.veri_duzeltme_detayi import VeriDuzeltmeDetayi

async def get_all_veri_duzeltme_detayi(db: AsyncSession):
    result = await db.execute(select(VeriDuzeltmeDetayi))
    return result.scalars().all()

async def get_veri_duzeltme_detayi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(VeriDuzeltmeDetayi).where(VeriDuzeltmeDetayi.id == id))
    return result.scalar_one_or_none()

async def create_veri_duzeltme_detayi(db: AsyncSession, obj: VeriDuzeltmeDetayi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj