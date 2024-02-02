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
    # ERRORS
    err = [

    ]
    # INLINES
    inl = [

    ]
    return msg + cb + inl + err
