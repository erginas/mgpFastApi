from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.teknik_resim_kapsami import TeknikResimKapsami

async def get_all_teknik_resim_kapsami(db: AsyncSession):
    result = await db.execute(select(TeknikResimKapsami))
    return result.scalars().all()

async def get_teknik_resim_kapsami_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TeknikResimKapsami).where(TeknikResimKapsami.id == id))
    return result.scalar_one_or_none()

async def create_teknik_resim_kapsami(db: AsyncSession, obj: TeknikResimKapsami):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj