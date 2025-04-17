from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.iptal_nedeni import IptalNedeni, IptalNedeniCreate
from models.iptal_nedeni import IptalNedeni as DBIptalNedeni
from crud.iptal_nedeni import get_all_iptal_nedeni, get_iptal_nedeni_by_id, create_iptal_nedeni

router = APIRouter(prefix='/iptal_nedeni', tags=['IptalNedeni'])

@router.get('/', response_model=list[IptalNedeni])
async def list_iptal_nedeni(db: AsyncSession = Depends()):
    return await get_all_iptal_nedeni(db)

@router.get('/{id}', response_model=IptalNedeni)
async def get_iptal_nedeni_item(id: int, db: AsyncSession = Depends()):
    result = await get_iptal_nedeni_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IptalNedeni)
async def create_iptal_nedeni_item(data: IptalNedeniCreate, db: AsyncSession = Depends()):
    db_item = DBIptalNedeni(**data.dict())
    return await create_iptal_nedeni(db, db_item)