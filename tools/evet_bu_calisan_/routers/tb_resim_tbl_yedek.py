from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tb_resim_tbl_yedek import TbResimTblYedek, TbResimTblYedekCreate
from models.tb_resim_tbl_yedek import TbResimTblYedek as DBTbResimTblYedek
from crud.tb_resim_tbl_yedek import get_all_tb_resim_tbl_yedek, get_tb_resim_tbl_yedek_by_id, create_tb_resim_tbl_yedek

router = APIRouter(prefix='/tb_resim_tbl_yedek', tags=['TbResimTblYedek'])

@router.get('/', response_model=list[TbResimTblYedek])
async def list_tb_resim_tbl_yedek(db: AsyncSession = Depends()):
    return await get_all_tb_resim_tbl_yedek(db)

@router.get('/{id}', response_model=TbResimTblYedek)
async def get_tb_resim_tbl_yedek_item(id: int, db: AsyncSession = Depends()):
    result = await get_tb_resim_tbl_yedek_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TbResimTblYedek)
async def create_tb_resim_tbl_yedek_item(data: TbResimTblYedekCreate, db: AsyncSession = Depends()):
    db_item = DBTbResimTblYedek(**data.dict())
    return await create_tb_resim_tbl_yedek(db, db_item)