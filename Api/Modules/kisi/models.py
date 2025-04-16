from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, CHAR, NVARCHAR
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Kisi(Base):
    __tablename__ = "kisi"  # Oracle tablonuzun ismi

    KIMLIK_NO = Column(Integer, primary_key=True)  # primary_key => Eğer KIMLIK_NO gerçekten birincil anahtar ise
    ADI = Column(String(80))
    SOYADI = Column(String(80))
    BABA_ADI = Column(String(80))
    ANA_ADI = Column(String(30))
    MESLEGI = Column(String(80))
    DOGUM_YERI = Column(String(80))
    DOGUM_TARIHI = Column(Date)
    KAN_GRUBU = Column(String(10))
    CINSIYETI = Column(CHAR(1))
    MEDENI_HALI = Column(String(10))
    EV_TEL = Column(String(50))
    CEP_TEL = Column(String(50))
    IS_TEL = Column(String(50))
    ADRES = Column(String(255))
    SSK_NO = Column(String(30))
    ILGILI_SIRKET = Column(String(5))
    ISE_GIRIS_TARIHI = Column(Date)
    ISTEN_CIKIS_T = Column(Date)
    VERGI_DAIRESI = Column(String(120))
    VERGI_NO = Column(String(20))
    BIRIM_NO = Column(Integer)
    GOREVI = Column(String(80))
    MESAI_FL = Column(CHAR(1))
    ACIKLAMA = Column(String(1024))
    GOREV_KODU = Column(Integer)
    EGITIM_DURUMU = Column(String(80))
    TAKMA_AD = Column(String(80))
    SIFRE = Column(String(255))
    AYAKKABI_NO = Column(String(10))
    UST_BEDEN = Column(String(10))
    ALT_BEDEN = Column(String(10))
    SIFRESI = Column(String(255))
    KILIT = Column(Integer)
    ID = Column(Integer)
    PASSWORD = Column(String(128))
    LAST_LOGIN = Column(TIMESTAMP)
    IS_SUPERUSER = Column(Integer)
    USERNAME = Column(NVARCHAR(150))
    FIRST_NAME = Column(NVARCHAR(150))
    EMAIL = Column(NVARCHAR(250))
    IS_STAFF = Column(Integer)
    IS_ACTIVE = Column(Integer)
    DATE_JOINED = Column(TIMESTAMP)
    AKTIF = Column(Integer)
    EKLEYEN_KULLANICI_KIMLIK_NO = Column(Integer)
    ENSONGUNCELLEYEN_KULLANICI_KIMLIK_NO = Column(Integer)
    EKLENME_ZAMANI = Column(TIMESTAMP)
    ENSON_GUNCELLENME_ZAMANI = Column(TIMESTAMP)
    MAC_ADDRESS = Column(String(48))
    GUNCELLEYEN_MAC_ADDRESS = Column(String(48))

class Kisi(BaseModel):
    KIMLIK_NO : Optional[int] = None
    ADI : Optional[str] = None
    SOYADI : Optional[str] = None
    BABA_ADI : Optional[str] = None
    ANA_ADI : Optional[str] = None
    MESLEGI : Optional[str] = None
    DOGUM_YERI : Optional[str] = None
    DOGUM_TARIHI :  Optional[datetime] = None
    KAN_GRUBU : Optional[str] = None
    CINSIYETI : Optional[str] = None
    MEDENI_HALI : Optional[str] = None
    EV_TEL : Optional[str] = None
    CEP_TEL : Optional[str] = None
    IS_TEL : Optional[str] = None
    ADRES : Optional[str] = None
    SSK_NO : Optional[str] = None
    ILGILI_SIRKET : Optional[str] = None
    ISE_GIRIS_TARIHI :  Optional[datetime] = None
    ISTEN_CIKIS_T :  Optional[datetime] = None
    VERGI_DAIRESI   : Optional[str] = None
    VERGI_NO        : Optional[str] = None
    BIRIM_NO        : Optional[int] = None
    GOREVI          : Optional[str] = None
    MESAI_FL        : Optional[str] = None
    ACIKLAMA        : Optional[str] = None
    GOREV_KODU      : Optional[int] = None
    EGITIM_DURUMU   : Optional[str] = None
    TAKMA_AD        : Optional[str] = None
    SIFRE           : Optional[str] = None
    AYAKKABI_NO     : Optional[str] = None
    UST_BEDEN       : Optional[str] = None
    ALT_BEDEN       : Optional[str] = None
    SIFRESI         : Optional[str] = None
    KILIT           : Optional[int] = None
    ID              : Optional[int] = None
    PASSWORD        : Optional[str] = None
    LAST_LOGIN      :  Optional[datetime] = None
    IS_SUPERUSER    : Optional[int] = None
    USERNAME        : Optional[str] = None
    FIRST_NAME      : Optional[str] = None
    EMAIL           : Optional[str] = None
    IS_STAFF        : Optional[int] = None
    IS_ACTIVE       : Optional[int] = None
    DATE_JOINED     :  Optional[datetime] = None
    AKTIF           : Optional[int] = None


