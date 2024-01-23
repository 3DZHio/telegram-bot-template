from src.database.core.functions import transaction, fetchone, fetchall


async def exists(uid: int) -> bool:
    """Check for Existence"""
    return bool(await fetchone("SELECT 1 FROM users WHERE uid = %s LIMIT 1;",
                               (uid,)))


async def add(uid: int) -> None:
    """Add"""
    await transaction("INSERT INTO users(uid) VALUES (%s);",
                      (uid,))


async def info(uid: int) -> dict:
    """Information"""
    return await fetchone("SELECT * FROM users WHERE uid = %s LIMIT 1;",
                          (uid,))
