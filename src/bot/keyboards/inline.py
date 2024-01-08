from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#
profile = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📼 Сохраненное", callback_data='fs')]
], row_width=1)
