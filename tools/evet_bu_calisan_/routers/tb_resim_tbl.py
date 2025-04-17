from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tb_resim_tbl import TbResimTbl, TbResimTblCreate
from models.tb_resim_tbl import TbResimTbl as DBTbResimTbl
from crud.tb_resim_tbl import get_all_tb_resim_tbl, get_tb_resim_tbl_by_id, create_tb_resim_tbl

router = APIRouter(prefix='/tb_resim_tbl', tags=['TbResimTbl'])

@router.get('/', response_model=list[TbResimTbl])
async def list_tb_resim_tbl(db: AsyncSession = Depends()):
    return await get_all_tb_resim_tbl(db)

@router.get('/{id}', response_model=TbResimTbl)
async def get_tb_resim_tbl_item(id: int, db: AsyncSession = Depends()):
    result = await get_tb_resim_tbl_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TbResimTbl)
async def create_tb_resim_tbl_item(data: TbResimTblCreate, db: AsyncSession = Depends()):
    db_item = DBTbResimTbl(**data.dict())
    return await create_tb_resim_tbl(db, db_item)