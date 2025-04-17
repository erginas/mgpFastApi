from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ariza_sabit import ArizaSabit

async def get_all_ariza_sabit(db: AsyncSession):
    result = await db.execute(select(ArizaSabit))
    return result.scalars().all()

async def get_ariza_sabit_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ArizaSabit).where(ArizaSabit.id == id))
    return result.scalar_one_or_none()

async def create_ariza_sabit(db: AsyncSession, obj: ArizaSabit):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj