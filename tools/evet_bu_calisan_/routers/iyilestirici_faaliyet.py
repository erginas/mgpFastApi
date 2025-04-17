from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.iyilestirici_faaliyet import IyilestiriciFaaliyet, IyilestiriciFaaliyetCreate
from models.iyilestirici_faaliyet import IyilestiriciFaaliyet as DBIyilestiriciFaaliyet
from crud.iyilestirici_faaliyet import get_all_iyilestirici_faaliyet, get_iyilestirici_faaliyet_by_id, create_iyilestirici_faaliyet

router = APIRouter(prefix='/iyilestirici_faaliyet', tags=['IyilestiriciFaaliyet'])

@router.get('/', response_model=list[IyilestiriciFaaliyet])
async def list_iyilestirici_faaliyet(db: AsyncSession = Depends()):
    return await get_all_iyilestirici_faaliyet(db)

@router.get('/{id}', response_model=IyilestiriciFaaliyet)
async def get_iyilestirici_faaliyet_item(id: int, db: AsyncSession = Depends()):
    result = await get_iyilestirici_faaliyet_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IyilestiriciFaaliyet)
async def create_iyilestirici_faaliyet_item(data: IyilestiriciFaaliyetCreate, db: AsyncSession = Depends()):
    db_item = DBIyilestiriciFaaliyet(**data.dict())
    return await create_iyilestirici_faaliyet(db, db_item)