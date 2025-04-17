from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.formul_degisken_degeri import FormulDegiskenDegeri

async def get_all_formul_degisken_degeri(db: AsyncSession):
    result = await db.execute(select(FormulDegiskenDegeri))
    return result.scalars().all()

async def get_formul_degisken_degeri_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FormulDegiskenDegeri).where(FormulDegiskenDegeri.id == id))
    return result.scalar_one_or_none()

async def create_formul_degisken_degeri(db: AsyncSession, obj: FormulDegiskenDegeri):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj