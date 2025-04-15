from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Menü öğesinin modelini tanımlayalım
class MenuItem(BaseModel):
    id: int
    title: str
    url: str

# Menü öğeleri listesi (bu veriyi veritabanından alabiliriz)
menu_items = [
    MenuItem(id=1, title="Ana Sayfa", url="/"),
    MenuItem(id=2, title="Hakkında", url="/about"),
    MenuItem(id=3, title="İletişim", url="/contact"),
    MenuItem(id=4, title="Kişi Listesi", url="/kisi/kisi-list"),
]

@router.get("/", response_model=List[MenuItem])
async def get_menu_items():
    return menu_items