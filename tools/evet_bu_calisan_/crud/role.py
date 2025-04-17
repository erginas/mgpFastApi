from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.role import Role

async def get_all_role(db: AsyncSession):
    result = await db.execute(select(Role))
    return result.scalars().all()

async def get_role_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Role).where(Role.id == id))
    return result.scalar_one_or_none()

async def create_role(db: AsyncSession, obj: Role):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj