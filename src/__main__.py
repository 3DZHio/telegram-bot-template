from asyncio import run
from contextlib import suppress

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.handlers import get_routers
from src.bot.utils import setup_logger, set_commands
from src.config import settings
from src.database.connection import pool


def setup_filters(dp: Dispatcher) -> None:
    """FILTERS"""

    dp.message.filter(F.chat.type == "private")  # Only Private Chat Filter


def setup_handlers(dp: Dispatcher) -> None:
    """HANDLERS"""

    dp.include_routers(*get_routers())  # Register Routers


def setup_middlewares(dp: Dispatcher) -> None:
    """MIDDLEWARES"""

    dp.message.middleware()  # Register MiddleWares


async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value(), parse_mode="HTML")  # Initializing Bot
    storage = MemoryStorage()  # Create Storage
    dp = Dispatcher(storage=storage)  # Launch Dispatcher

    setup_logger("INFO", ["aiogram.bot.api"])  # Logging
    setup_filters(dp)  # Filters
    setup_handlers(dp)  # Handlers
    setup_middlewares(dp)  # MiddleWares
    await set_commands(bot)  # Bot Commands

    try:
        await pool.open()  # Open Connection Pool
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())  # Start Polling
    finally:
        await pool.close()  # Close Connection Pool
        await dp.storage.close()  # Close Storage
        await bot.session.close()  # Close Bot Session


if __name__ == '__main__':  # Entry Point
    with suppress(KeyboardInterrupt, SystemExit):  # Suppress KeyboardInterrupt and SystemExit Exceptions
        run(main())  # Launch Code
