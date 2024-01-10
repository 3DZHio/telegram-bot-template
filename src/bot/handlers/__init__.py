from aiogram import Router

from src.bot.handlers import callbacks, commands, errors, inline_mode


def get_routers() -> list[Router]:
    return [
        commands.start_router,
        commands.help_router,
        commands.settings_router,
    ]
