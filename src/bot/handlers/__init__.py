from aiogram import Router

from src.bot.handlers import callbacks, messages, errors, inlines


def get_routers() -> list[Router]:
    # CallBacks
    cb_routers = [
        callbacks.router,
    ]
    # Commands
    cmd_routers = [
        messages.start_router,
        messages.router,
    ]
    # Errors
    err_routers = [
        errors.router,
    ]
    # Inline Mode
    inl_routers = [
        inlines.router,
    ]
    return cb_routers + cmd_routers + err_routers + inl_routers
