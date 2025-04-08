from pydantic import BaseModel
from typing import Optional


class Aktarma(BaseModel):
    stok_kodu : Optional[str] = None
    malzeme_no : Optional[int] = None
