from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.misc.routers import start_router
from src.bot.texts import outer
from src.database.models import users

router = Router()


@start_router.message(CommandStart(), F.text)
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if not (await users.exists(uid)):
        await users.add(uid)
    await message.answer(text=outer.start)
