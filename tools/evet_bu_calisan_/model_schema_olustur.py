import re
from pathlib import Path

import sqlalchemy
from sqlalchemy import MetaData, inspect
from sqlalchemy.orm import declarative_base

# 🎯 Ayarlar
ORACLE_USERNAME = "mgp"
ORACLE_PASSWORD = "mgp"
ORACLE_DSN = "192.168.0.253:1521/tpsn"

Base = declarative_base()

# 📁 Çıktı dizinleri
Path("models").mkdir(exist_ok=True)
Path("schemas").mkdir(exist_ok=True)
Path("crud").mkdir(exist_ok=True)
Path("routers").mkdir(exist_ok=True)


def snake_to_pascal(name):
    return ''.join(word.capitalize() for word in name.split('_'))


def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def map_sql_type(col):
    coltype = str(col.type)
    precision = getattr(col.type, "precision", None)

    if "NUMBER" in coltype:
        return "Float" if precision and precision > 0 else "Integer"
    elif "DATE" in coltype or "TIMESTAMP" in coltype:
        return "DateTime"
    elif "CHAR" in coltype or "CLOB" in coltype:
        return "String"
    else:
        return "String"


def generate_model_code(table, inspector):
    class_name = snake_to_pascal(table.name)
    lines = [f"class {class_name}(Base):", f"    __tablename__ = '{table.name}'", ""]
    for col in table.columns:
        col_type = map_sql_type(col)
        nullable = ", nullable=False" if not col.nullable else ""
        lines.append(f"    {col.name}: Mapped[Optional[{col_type}]] = mapped_column({col_type}{nullable})")

    fks = inspector.get_foreign_keys(table.name)
    used_names = set()
    for fk in fks:
        target = fk["referred_table"]
        rel_var = camel_to_snake(target)
        count = 1
        while rel_var in used_names:
            rel_var = f"{rel_var}_{count}"
            count += 1
        used_names.add(rel_var)
        lines.append(
            f"    {rel_var}: Mapped[Optional['{snake_to_pascal(target)}']] = relationship(back_populates='{table.name}')")

    return "\n".join(lines)


def generate_schema_code(table):
    class_name = snake_to_pascal(table.name)
    lines = [f"class {class_name}Base(BaseModel):"]
    for col in table.columns:
        col_type = map_sql_type(col)
        lines.append(f"    {col.name}: Optional[{col_type}] = None")
    lines += ["", f"class {class_name}Create({class_name}Base):", "    pass", "",
              f"class {class_name}({class_name}Base):", "    id: Optional[int]", "",
              "    class Config:", "        orm_mode = True"]
    return "\n".join(lines)


def generate_crud_code(table):
    name = table.name
    class_name = snake_to_pascal(name)
    lines = [
        f"from sqlalchemy.ext.asyncio import AsyncSession",
        f"from sqlalchemy.future import select",
        f"from models.{name} import {class_name}",
        "",
        f"async def get_all_{name}(db: AsyncSession):",
        f"    result = await db.execute(select({class_name}))",
        f"    return result.scalars().all()",
        "",
        f"async def get_{name}_by_id(db: AsyncSession, id: int):",
        f"    result = await db.execute(select({class_name}).where({class_name}.id == id))",
        f"    return result.scalar_one_or_none()",
        "",
        f"async def create_{name}(db: AsyncSession, obj: {class_name}):",
        f"    db.add(obj)",
        f"    await db.commit()",
        f"    await db.refresh(obj)",
        f"    return obj"
    ]
    return "\n".join(lines)


def generate_router_code(table):
    name = table.name
    class_name = snake_to_pascal(name)
    lines = [
        f"from fastapi import APIRouter, Depends, HTTPException",
        f"from sqlalchemy.ext.asyncio import AsyncSession",
        f"from schemas.{name} import {class_name}, {class_name}Create",
        f"from models.{name} import {class_name} as DB{class_name}",
        f"from crud.{name} import get_all_{name}, get_{name}_by_id, create_{name}",
        "",
        f"router = APIRouter(prefix='/{name}', tags=['{class_name}'])",
        "",
        f"@router.get('/', response_model=list[{class_name}])",
        f"async def list_{name}(db: AsyncSession = Depends()):",
        f"    return await get_all_{name}(db)",
        "",
        f"@router.get('/{{id}}', response_model={class_name})",
        f"async def get_{name}_item(id: int, db: AsyncSession = Depends()):",
        f"    result = await get_{name}_by_id(db, id)",
        f"    if not result: raise HTTPException(404, detail='Not found')",
        f"    return result",
        "",
        f"@router.post('/', response_model={class_name})",
        f"async def create_{name}_item(data: {class_name}Create, db: AsyncSession = Depends()):",
        f"    db_item = DB{class_name}(**data.dict())",
        f"    return await create_{name}(db, db_item)"
    ]
    return "\n".join(lines)


def main():
    engine = sqlalchemy.create_engine(f'oracle+oracledb://{ORACLE_USERNAME}:{ORACLE_PASSWORD}@{ORACLE_DSN}')
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)

    for table_name, table in metadata.tables.items():
        print(f"🚀 {table_name} işleniyor...")

        class_name = snake_to_pascal(table_name)

        with open(f"models/{table_name}.py", "w", encoding="utf-8") as f:
            f.write("from sqlalchemy.orm import Mapped, mapped_column, relationship\n")
            f.write("from sqlalchemy import String, Integer, Float, DateTime\n")
            f.write("from sqlalchemy.orm import declarative_base\n\n")
            f.write("Base = declarative_base()\n\n")
            f.write(generate_model_code(table, inspector))

        with open(f"schemas/{table_name}.py", "w", encoding="utf-8") as f:
            f.write("from pydantic import BaseModel\n")
            f.write("from typing import Optional\n\n")
            f.write(generate_schema_code(table))

        with open(f"crud/{table_name}.py", "w", encoding="utf-8") as f:
            f.write(generate_crud_code(table))

        with open(f"routers/{table_name}.py", "w", encoding="utf-8") as f:
            f.write(generate_router_code(table))

    print("\n✅ Tüm tablolar işlendi!")


if __name__ == "__main__":
    main()
