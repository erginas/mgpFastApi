from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tmp_resim_olcusu import TmpResimOlcusu, TmpResimOlcusuCreate
from models.tmp_resim_olcusu import TmpResimOlcusu as DBTmpResimOlcusu
from crud.tmp_resim_olcusu import get_all_tmp_resim_olcusu, get_tmp_resim_olcusu_by_id, create_tmp_resim_olcusu

router = APIRouter(prefix='/tmp_resim_olcusu', tags=['TmpResimOlcusu'])

@router.get('/', response_model=list[TmpResimOlcusu])
async def list_tmp_resim_olcusu(db: AsyncSession = Depends()):
    return await get_all_tmp_resim_olcusu(db)

@router.get('/{id}', response_model=TmpResimOlcusu)
async def get_tmp_resim_olcusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_tmp_resim_olcusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TmpResimOlcusu)
async def create_tmp_resim_olcusu_item(data: TmpResimOlcusuCreate, db: AsyncSession = Depends()):
    db_item = DBTmpResimOlcusu(**data.dict())
    return await create_tmp_resim_olcusu(db, db_item)