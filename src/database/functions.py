from psycopg.rows import dict_row

from src.database.connection import pool


async def transaction(query: str, params: tuple) -> None:
    """Transaction"""
    async with pool.connection() as conn:
        async with conn.transaction():
            await conn.execute(query, params)


async def fetchall(query: str, params: tuple) -> dict:
    """FetchAll"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, params)
            return (await cursor.fetchall())[0]
