from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.utt import Utt, UttCreate
from models.utt import Utt as DBUtt
from crud.utt import get_all_utt, get_utt_by_id, create_utt

router = APIRouter(prefix='/utt', tags=['Utt'])

@router.get('/', response_model=list[Utt])
async def list_utt(db: AsyncSession = Depends()):
    return await get_all_utt(db)

@router.get('/{id}', response_model=Utt)
async def get_utt_item(id: int, db: AsyncSession = Depends()):
    result = await get_utt_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Utt)
async def create_utt_item(data: UttCreate, db: AsyncSession = Depends()):
    db_item = DBUtt(**data.dict())
    return await create_utt(db, db_item)