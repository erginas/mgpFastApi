from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"

@compiles(utcnow, "oracle")
def oracle_utcnow(element, compiler, **kw):
    return "SYS_EXTRACT_UTC(SYSTIMESTAMP)"

@compiles(utcnow, "mysql")
def mysql_utcnow(element, compiler, **kw):
    return "UTC_TIMESTAMP()"

@compiles(utcnow, "sqlite")
def sqlite_utcnow(element, compiler, **kw):
    return "(strftime('%Y-%m-%d %H:%M:%f', 'now'))"