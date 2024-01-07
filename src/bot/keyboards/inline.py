from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def inline_keyboard_markup(inline_keyboard: list[list[InlineKeyboardButton]]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
