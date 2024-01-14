from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand

from src.bot.texts.ru import bot_commands


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command=command, description=description)
        for command, description in bot_commands.items()
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())
