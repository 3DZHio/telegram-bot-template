from asyncio import WindowsSelectorEventLoopPolicy, set_event_loop_policy

from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool
from pydantic import PostgresDsn

from src.config import settings

set_event_loop_policy(WindowsSelectorEventLoopPolicy())  # For DataBase on Windows

DSN: PostgresDsn = (
    "postgresql://"
    f"{settings.USER.get_secret_value()}"
    f":{settings.PASSWORD.get_secret_value()}"
    f"@{settings.HOST.get_secret_value()}"
    f":{settings.PORT.get_secret_value()}"
    f"/{settings.DATABASE.get_secret_value()}"
)

pool = AsyncConnectionPool(conninfo=DSN, open=False)


async def transaction(query: str, args: tuple) -> None:
    """Transaction"""
    async with pool.connection() as conn:
        async with conn.transaction():
            await conn.execute(query, args)


async def fetchall(query: str, args: tuple) -> dict:
    """FetchAll"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, args)
            return list(await cursor.fetchall())[0]
