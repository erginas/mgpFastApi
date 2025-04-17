from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.permission import Permission

async def get_all_permission(db: AsyncSession):
    result = await db.execute(select(Permission))
    return result.scalars().all()

async def get_permission_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Permission).where(Permission.id == id))
    return result.scalar_one_or_none()

async def create_permission(db: AsyncSession, obj: Permission):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj