from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aktar_iade import AktarIade, AktarIadeCreate
from models.aktar_iade import AktarIade as DBAktarIade
from crud.aktar_iade import get_all_aktar_iade, get_aktar_iade_by_id, create_aktar_iade

router = APIRouter(prefix='/aktar_iade', tags=['AktarIade'])

@router.get('/', response_model=list[AktarIade])
async def list_aktar_iade(db: AsyncSession = Depends()):
    return await get_all_aktar_iade(db)

@router.get('/{id}', response_model=AktarIade)
async def get_aktar_iade_item(id: int, db: AsyncSession = Depends()):
    result = await get_aktar_iade_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AktarIade)
async def create_aktar_iade_item(data: AktarIadeCreate, db: AsyncSession = Depends()):
    db_item = DBAktarIade(**data.dict())
    return await create_aktar_iade(db, db_item)