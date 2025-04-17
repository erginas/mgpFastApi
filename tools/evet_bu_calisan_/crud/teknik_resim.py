from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.teknik_resim import TeknikResim

async def get_all_teknik_resim(db: AsyncSession):
    result = await db.execute(select(TeknikResim))
    return result.scalars().all()

async def get_teknik_resim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TeknikResim).where(TeknikResim.id == id))
    return result.scalar_one_or_none()

async def create_teknik_resim(db: AsyncSession, obj: TeknikResim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj