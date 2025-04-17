from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.operasyon_checklist import OperasyonChecklist

async def get_all_operasyon_checklist(db: AsyncSession):
    result = await db.execute(select(OperasyonChecklist))
    return result.scalars().all()

async def get_operasyon_checklist_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(OperasyonChecklist).where(OperasyonChecklist.id == id))
    return result.scalar_one_or_none()

async def create_operasyon_checklist(db: AsyncSession, obj: OperasyonChecklist):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj