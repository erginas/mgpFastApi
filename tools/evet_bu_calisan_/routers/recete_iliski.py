from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_iliski import ReceteIliski, ReceteIliskiCreate
from models.recete_iliski import ReceteIliski as DBReceteIliski
from crud.recete_iliski import get_all_recete_iliski, get_recete_iliski_by_id, create_recete_iliski

router = APIRouter(prefix='/recete_iliski', tags=['ReceteIliski'])

@router.get('/', response_model=list[ReceteIliski])
async def list_recete_iliski(db: AsyncSession = Depends()):
    return await get_all_recete_iliski(db)

@router.get('/{id}', response_model=ReceteIliski)
async def get_recete_iliski_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_iliski_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteIliski)
async def create_recete_iliski_item(data: ReceteIliskiCreate, db: AsyncSession = Depends()):
    db_item = DBReceteIliski(**data.dict())
    return await create_recete_iliski(db, db_item)