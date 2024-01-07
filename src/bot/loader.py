from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.config import settings  # Prerequisites

bot = Bot(token=settings.BOT_TOKEN.get_secret_value(), parse_mode="HTML")  # Initializing Bot
storage = MemoryStorage()  # Create Storage
dp = Dispatcher(storage=storage)  # Launch Dispatcher
