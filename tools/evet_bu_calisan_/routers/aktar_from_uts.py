from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aktar_from_uts import AktarFromUts, AktarFromUtsCreate
from models.aktar_from_uts import AktarFromUts as DBAktarFromUts
from crud.aktar_from_uts import get_all_aktar_from_uts, get_aktar_from_uts_by_id, create_aktar_from_uts

router = APIRouter(prefix='/aktar_from_uts', tags=['AktarFromUts'])

@router.get('/', response_model=list[AktarFromUts])
async def list_aktar_from_uts(db: AsyncSession = Depends()):
    return await get_all_aktar_from_uts(db)

@router.get('/{id}', response_model=AktarFromUts)
async def get_aktar_from_uts_item(id: int, db: AsyncSession = Depends()):
    result = await get_aktar_from_uts_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AktarFromUts)
async def create_aktar_from_uts_item(data: AktarFromUtsCreate, db: AsyncSession = Depends()):
    db_item = DBAktarFromUts(**data.dict())
    return await create_aktar_from_uts(db, db_item)