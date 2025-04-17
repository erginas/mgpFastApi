from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_teslimi import AlinanSiparisTeslimi

async def get_all_alinan_siparis_teslimi(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisTeslimi))
    return result.scalars().all()

async def get_alinan_siparis_teslimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisTeslimi).where(AlinanSiparisTeslimi.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_teslimi(db: AsyncSession, obj: AlinanSiparisTeslimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj