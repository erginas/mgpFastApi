from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.django_migrations import DjangoMigrations

async def get_all_django_migrations(db: AsyncSession):
    result = await db.execute(select(DjangoMigrations))
    return result.scalars().all()

async def get_django_migrations_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DjangoMigrations).where(DjangoMigrations.id == id))
    return result.scalar_one_or_none()

async def create_django_migrations(db: AsyncSession, obj: DjangoMigrations):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj