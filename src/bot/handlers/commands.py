from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.misc.routers import start_router
from src.database.models import users


@start_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if not (await users.exists(uid)):
        await users.add(uid)
    await message.answer(text="Start")
