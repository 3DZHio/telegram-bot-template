from aiogram import Router

from src.bot.handlers import commands


def get_routers() -> list[Router]:
    return [
        commands.start,
    ]
