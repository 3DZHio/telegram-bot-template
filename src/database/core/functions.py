from psycopg.rows import dict_row

from src.database.core.connection import pool


async def transaction(query: str, params: tuple = None) -> None:
    """Transaction"""
    async with pool.connection() as conn:
        async with conn.transaction():
            await conn.execute(query, params)


async def fetchone(query: str, params: tuple = None) -> dict:
    """FetchOne"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchone()


async def fetchall(query: str, params: tuple = None) -> list[dict]:
    """FetchAll"""
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cursor:
            await cursor.execute(query, params)
            return await cursor.fetchall()


def select(columns: str, table: str, conditions: str, offset: str = "0", limit: str = "1") -> str:
    """ SELECT """
    return f"SELECT {columns} FROM {table} WHERE {conditions} OFFSET {offset} LIMIT {limit};"


def insert(table: str, columns: str, values: str) -> str:
    """ INSERT """
    return f"INSERT INTO {table} ({columns}) VALUES ({values});"


def update(table: str, column: str, value: str, conditions: str) -> str:
    """ UPDATE """
    return f"UPDATE {table} SET {column} = {value} WHERE {conditions};"
