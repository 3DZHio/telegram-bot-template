from src.database.core.functions import transaction, fetchone, fetchall


async def exists(uid: int) -> bool:
    """Проверить на Существование"""
    return bool(await fetchone("SELECT true FROM users WHERE uid = %s;",
                               (uid,)))


async def add(uid: int) -> None:
    """Добавить"""
    await transaction("INSERT INTO users(uid) VALUES (%s);",
                      (uid,))


async def info(uid: int) -> dict:
    """Информация"""
    return await fetchone("SELECT * FROM users WHERE uid = %s;",
                          (uid,))
