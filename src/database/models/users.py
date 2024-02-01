from src.database.core import functions


async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await functions.fetchone("SELECT 1 FROM users WHERE uid = %s LIMIT 1;",
                                         (uid,)))


async def add(uid: int) -> None:
    """Add"""
    await functions.transaction("INSERT INTO users(uid) VALUES (%s);",
                                (uid,))


async def info(uid: int) -> dict:
    """Information"""
    return await functions.fetchone("SELECT * FROM users WHERE uid = %s LIMIT 1;",
                                    (uid,))
