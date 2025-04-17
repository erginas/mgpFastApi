from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.iptal_nedeni import IptalNedeni

async def get_all_iptal_nedeni(db: AsyncSession):
    result = await db.execute(select(IptalNedeni))
    return result.scalars().all()

async def get_iptal_nedeni_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IptalNedeni).where(IptalNedeni.id == id))
    return result.scalar_one_or_none()

async def create_iptal_nedeni(db: AsyncSession, obj: IptalNedeni):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj