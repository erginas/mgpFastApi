from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.organizasyon_birimi import OrganizasyonBirimi

async def get_all_organizasyon_birimi(db: AsyncSession):
    result = await db.execute(select(OrganizasyonBirimi))
    return result.scalars().all()

async def get_organizasyon_birimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(OrganizasyonBirimi).where(OrganizasyonBirimi.id == id))
    return result.scalar_one_or_none()

async def create_organizasyon_birimi(db: AsyncSession, obj: OrganizasyonBirimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj