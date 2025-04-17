from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tedarikci_degerlendirmesi import TedarikciDegerlendirmesi

async def get_all_tedarikci_degerlendirmesi(db: AsyncSession):
    result = await db.execute(select(TedarikciDegerlendirmesi))
    return result.scalars().all()

async def get_tedarikci_degerlendirmesi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TedarikciDegerlendirmesi).where(TedarikciDegerlendirmesi.id == id))
    return result.scalar_one_or_none()

async def create_tedarikci_degerlendirmesi(db: AsyncSession, obj: TedarikciDegerlendirmesi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj