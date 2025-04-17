from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_urun_agaci import ReceteUrunAgaci

async def get_all_recete_urun_agaci(db: AsyncSession):
    result = await db.execute(select(ReceteUrunAgaci))
    return result.scalars().all()

async def get_recete_urun_agaci_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteUrunAgaci).where(ReceteUrunAgaci.id == id))
    return result.scalar_one_or_none()

async def create_recete_urun_agaci(db: AsyncSession, obj: ReceteUrunAgaci):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj