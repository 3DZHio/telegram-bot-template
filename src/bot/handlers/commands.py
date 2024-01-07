from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.database import users

start = Router()


@start.message(CommandStart())
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if await users.exists(uid):
        await message.answer(text="first_intro")
    else:
        await users.add(uid)
        await message.answer(text="second_intro")
