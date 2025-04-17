from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete import Recete, ReceteCreate
from models.recete import Recete as DBRecete
from crud.recete import get_all_recete, get_recete_by_id, create_recete

router = APIRouter(prefix='/recete', tags=['Recete'])

@router.get('/', response_model=list[Recete])
async def list_recete(db: AsyncSession = Depends()):
    return await get_all_recete(db)

@router.get('/{id}', response_model=Recete)
async def get_recete_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Recete)
async def create_recete_item(data: ReceteCreate, db: AsyncSession = Depends()):
    db_item = DBRecete(**data.dict())
    return await create_recete(db, db_item)