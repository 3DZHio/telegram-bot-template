from src.database.core.functions import fetchone, transaction, select
from src.database.text import all_columns, any_columns, users, uid_condition


async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await fetchone(select(any_columns, users, uid_condition),
                               (uid,)))


async def add(uid: int) -> None:
    """Add"""
    await transaction("INSERT INTO users(uid) VALUES (%s);",
                      (uid,))


async def info(uid: int) -> dict:
    """Information"""
    return await fetchone(select(all_columns, users, uid_condition),
                          (uid,))
