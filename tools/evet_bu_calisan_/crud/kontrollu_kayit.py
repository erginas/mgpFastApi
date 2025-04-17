from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kontrollu_kayit import KontrolluKayit

async def get_all_kontrollu_kayit(db: AsyncSession):
    result = await db.execute(select(KontrolluKayit))
    return result.scalars().all()

async def get_kontrollu_kayit_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KontrolluKayit).where(KontrolluKayit.id == id))
    return result.scalar_one_or_none()

async def create_kontrollu_kayit(db: AsyncSession, obj: KontrolluKayit):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj