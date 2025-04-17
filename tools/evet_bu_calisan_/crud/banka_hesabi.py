from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.banka_hesabi import BankaHesabi

async def get_all_banka_hesabi(db: AsyncSession):
    result = await db.execute(select(BankaHesabi))
    return result.scalars().all()

async def get_banka_hesabi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(BankaHesabi).where(BankaHesabi.id == id))
    return result.scalar_one_or_none()

async def create_banka_hesabi(db: AsyncSession, obj: BankaHesabi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj