from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.misc import routers
from src.bot.texts import outer
from src.database.models import users


# START
@routers.msg_start.message(CommandStart(), F.text)
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if not (await users.exists(uid)):
        await users.add(uid)
    await message.answer(text=outer.start)
