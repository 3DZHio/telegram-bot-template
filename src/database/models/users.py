from src.database.core.functions import fetchall, transaction


async def exists(uid: int) -> bool:
    """Проверить на Существование"""
    return bool(await fetchall("SELECT true FROM users WHERE uid = %s;",
                               (uid,)))


async def add(uid: int) -> None:
    """Добавить"""
    await transaction("INSERT INTO users(uid) VALUES (%s);",
                      (uid,))


async def info(uid: int) -> dict:
    """Информация"""
    return await fetchall("SELECT * FROM users WHERE uid = %s;",
                          (uid,))
