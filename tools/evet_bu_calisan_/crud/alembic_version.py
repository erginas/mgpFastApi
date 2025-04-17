from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alembic_version import AlembicVersion

async def get_all_alembic_version(db: AsyncSession):
    result = await db.execute(select(AlembicVersion))
    return result.scalars().all()

async def get_alembic_version_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlembicVersion).where(AlembicVersion.id == id))
    return result.scalar_one_or_none()

async def create_alembic_version(db: AsyncSession, obj: AlembicVersion):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj