from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_aktarma_islemi import IsEmriAktarmaIslemi

async def get_all_is_emri_aktarma_islemi(db: AsyncSession):
    result = await db.execute(select(IsEmriAktarmaIslemi))
    return result.scalars().all()

async def get_is_emri_aktarma_islemi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriAktarmaIslemi).where(IsEmriAktarmaIslemi.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_aktarma_islemi(db: AsyncSession, obj: IsEmriAktarmaIslemi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj