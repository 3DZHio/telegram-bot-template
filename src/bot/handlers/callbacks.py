from aiogram import F
from aiogram.types import CallbackQuery

from src.bot.misc.routers import callbacks_router


@callbacks_router.callback_query(F.data == 'a')
async def cb_a(callback: CallbackQuery) -> None:
    await callback.message.delete()
    await callback.message.answer(text="a")
