import oracledb
import os
from dotenv import load_dotenv
from dotenv import dotenv_values


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_connection():
    return oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )

# print(dotenv_path)
# print(load_dotenv(dotenv_path))
#
# print("USER:", os.getenv("ORACLE_USER"))