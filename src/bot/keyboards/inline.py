from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="a", callback_data='a')],

    [InlineKeyboardButton(text="b", callback_data='b'),
     InlineKeyboardButton(text="c", callback_data='c')],

    [InlineKeyboardButton(text="d", callback_data='d')]
], row_width=1)

# a
# b c
# d
