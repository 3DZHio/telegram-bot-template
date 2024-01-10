from aiogram import Router

from src.bot.handlers import callbacks, commands, errors, inline_mode


def get_routers() -> list[Router]:
    # CallBacks
    cb_routers = [
        callbacks.router,
    ]
    # Commands
    cmd_routers = [
        commands.router,
        commands.start_router,
        commands.help_router,
        commands.settings_router
    ]
    # Errors
    err_routers = [
        errors.router,
    ]
    # Inline Mode
    inl_routers = [
        inline_mode.router,
    ]
    return cb_routers + cmd_routers + err_routers + inl_routers
