from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ozellik_secenegi import OzellikSecenegi

async def get_all_ozellik_secenegi(db: AsyncSession):
    result = await db.execute(select(OzellikSecenegi))
    return result.scalars().all()

async def get_ozellik_secenegi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(OzellikSecenegi).where(OzellikSecenegi.id == id))
    return result.scalar_one_or_none()

async def create_ozellik_secenegi(db: AsyncSession, obj: OzellikSecenegi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj