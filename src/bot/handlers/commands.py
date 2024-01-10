from aiogram import F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.bot.misc.routers import start_router, help_router, settings_router
from src.database.models import users


@start_router.message(F.text, CommandStart())
async def cmd_start(message: Message) -> None:
    uid = message.chat.id
    await message.delete()
    if not (await users.exists(uid)):
        await users.add(uid)
    await message.answer(text="Start")


@help_router.message(F.text, Command("help"))
async def cmd_help(message: Message) -> None:
    await message.delete()
    await message.answer(text="Help")


@settings_router.message(F.text, Command("settings"))
async def cmd_settings(message: Message) -> None:
    await message.delete()
    await message.answer(text="Settings")
