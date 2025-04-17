from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.users import Users

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(Users))
    return result.scalars().all()

async def get_users_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Users).where(Users.id == id))
    return result.scalar_one_or_none()

async def create_users(db: AsyncSession, obj: Users):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj