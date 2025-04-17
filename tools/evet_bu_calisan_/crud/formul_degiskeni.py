from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.formul_degiskeni import FormulDegiskeni

async def get_all_formul_degiskeni(db: AsyncSession):
    result = await db.execute(select(FormulDegiskeni))
    return result.scalars().all()

async def get_formul_degiskeni_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FormulDegiskeni).where(FormulDegiskeni.id == id))
    return result.scalar_one_or_none()

async def create_formul_degiskeni(db: AsyncSession, obj: FormulDegiskeni):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj