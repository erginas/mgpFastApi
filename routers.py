from fastapi import APIRouter
from typing import List

from sqlalchemy.testing.suite.test_reflection import users

from alinan_iade.models import Aktarma
from app.crud import get_all_malzeme
from malzeme_test.crud import xget_all_malzeme
from malzeme_test.models import Malzeme
from alinan_iade.crud import get_all_data, insert_data, update_data, delete_data




router = APIRouter()



@router.get("/malzemeler", response_model=List[Malzeme])
def list_malzeme():
    return get_all_malzeme()


@router.get("/xmalzemeler", response_model=List[Malzeme])
def list_malzeme():
    return xget_all_malzeme()

@router.get("/aktarma-list", response_model=List[Aktarma])
def list_aktarma():
    return get_all_data()

@router.post("/aktarma")
def add_data(data: Aktarma):
    return insert_data(data)

@router.put("/aktarma/{malzeme_no}")
def modify_data(malzeme_no: int, data: Aktarma):
    return update_data(malzeme_no, data)

@router.delete("/aktarma/{malzeme_no}")
def remove_data(malzeme_no: int):
    return delete_data(malzeme_no)

