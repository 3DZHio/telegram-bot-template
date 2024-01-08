from src.bot.loader import bot, dp
from src.database.connection import pool


def setup_filters() -> None:
    """FILTERS"""
    from aiogram import F

    dp.message.filter(F.chat.type == "private")  # Only Private Chat Filter


def setup_handlers() -> None:
    """HANDLERS"""
    from src.bot.handlers import get_routers

    dp.include_routers(*get_routers())  # Register Routers


def setup_middlewares() -> None:
    """MIDDLEWARES"""
    dp.message.middleware()


@dp.startup()
async def on_startup() -> None:
    """STARTUP"""
    from src.bot.utils import setup_logger, set_commands

    setup_logger("INFO", ["aiogram.bot.api"])  # Logging
    setup_filters()  # Filters
    setup_handlers()  # Handlers
    setup_middlewares()  # MiddleWares
    await set_commands(bot)  # Bot Commands
    await pool.open()  # Open Connection Pool


@dp.shutdown()
async def on_shutdown() -> None:
    """SHUTDOWN"""
    await dp.storage.close()  # Close Storage
    await pool.close()  # Close Connection Pool
    await bot.session.close()  # Close Bot Session


if __name__ == '__main__':  # Entry Point
    from asyncio import run

    run(dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()))  # Start Polling
