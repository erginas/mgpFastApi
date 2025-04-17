from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_teslimi import AlinanSiparisTeslimi, AlinanSiparisTeslimiCreate
from models.alinan_siparis_teslimi import AlinanSiparisTeslimi as DBAlinanSiparisTeslimi
from crud.alinan_siparis_teslimi import get_all_alinan_siparis_teslimi, get_alinan_siparis_teslimi_by_id, create_alinan_siparis_teslimi

router = APIRouter(prefix='/alinan_siparis_teslimi', tags=['AlinanSiparisTeslimi'])

@router.get('/', response_model=list[AlinanSiparisTeslimi])
async def list_alinan_siparis_teslimi(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_teslimi(db)

@router.get('/{id}', response_model=AlinanSiparisTeslimi)
async def get_alinan_siparis_teslimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_teslimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisTeslimi)
async def create_alinan_siparis_teslimi_item(data: AlinanSiparisTeslimiCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisTeslimi(**data.dict())
    return await create_alinan_siparis_teslimi(db, db_item)