from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tedarikci_emri import TedarikciEmri

async def get_all_tedarikci_emri(db: AsyncSession):
    result = await db.execute(select(TedarikciEmri))
    return result.scalars().all()

async def get_tedarikci_emri_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TedarikciEmri).where(TedarikciEmri.id == id))
    return result.scalar_one_or_none()

async def create_tedarikci_emri(db: AsyncSession, obj: TedarikciEmri):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj