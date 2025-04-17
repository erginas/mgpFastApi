from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.bilgisayar import Bilgisayar

async def get_all_bilgisayar(db: AsyncSession):
    result = await db.execute(select(Bilgisayar))
    return result.scalars().all()

async def get_bilgisayar_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Bilgisayar).where(Bilgisayar.id == id))
    return result.scalar_one_or_none()

async def create_bilgisayar(db: AsyncSession, obj: Bilgisayar):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj