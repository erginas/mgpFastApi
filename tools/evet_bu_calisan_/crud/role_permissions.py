from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.role_permissions import RolePermissions

async def get_all_role_permissions(db: AsyncSession):
    result = await db.execute(select(RolePermissions))
    return result.scalars().all()

async def get_role_permissions_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(RolePermissions).where(RolePermissions.id == id))
    return result.scalar_one_or_none()

async def create_role_permissions(db: AsyncSession, obj: RolePermissions):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj