from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ozellik_sablonu import OzellikSablonu

async def get_all_ozellik_sablonu(db: AsyncSession):
    result = await db.execute(select(OzellikSablonu))
    return result.scalars().all()

async def get_ozellik_sablonu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(OzellikSablonu).where(OzellikSablonu.id == id))
    return result.scalar_one_or_none()

async def create_ozellik_sablonu(db: AsyncSession, obj: OzellikSablonu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj