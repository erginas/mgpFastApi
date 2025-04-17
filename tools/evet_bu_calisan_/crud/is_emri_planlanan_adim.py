from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_planlanan_adim import IsEmriPlanlananAdim

async def get_all_is_emri_planlanan_adim(db: AsyncSession):
    result = await db.execute(select(IsEmriPlanlananAdim))
    return result.scalars().all()

async def get_is_emri_planlanan_adim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriPlanlananAdim).where(IsEmriPlanlananAdim.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_planlanan_adim(db: AsyncSession, obj: IsEmriPlanlananAdim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj