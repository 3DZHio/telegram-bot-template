from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.database import users

start = Router(name="start-router")


@start.message(CommandStart())
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if not (await users.exists(uid)):
        await users.add(uid)
    await message.answer(text="Start")
