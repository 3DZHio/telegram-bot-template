from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
    # MESSAGES
    msg = [
        messages.routers.msg_start,
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
