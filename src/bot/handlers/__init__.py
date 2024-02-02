from aiogram import Router

from src.bot.handlers import callbacks, messages, errors, inlines


def get_routers() -> list[Router]:
    # MESSAGES
    msg = [
        messages.routers.start,
    ]
    # CALLBACKS
    cb = [

    ]
    # INLINES
    inl = [

    ]
    # ERRORS
    err = [

    ]
    return msg + cb + inl + err
