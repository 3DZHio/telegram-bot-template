from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def reply_keyboard_markup(keyboard: list[list[KeyboardButton]],
                          resize_keyboard: bool = True,
                          input_field_placeholder: str | None = None) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(keyboard=keyboard,
                               resize_keyboard=resize_keyboard,
                               input_field_placeholder=input_field_placeholder)
