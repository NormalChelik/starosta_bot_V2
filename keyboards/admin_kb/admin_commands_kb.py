from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = [[InlineKeyboardButton(text="🗒 Расписание", callback_data="raspisanye_kb")],
            [InlineKeyboardButton(text="🔔 Заверить отметившихся", callback_data="zaverit_kb"), InlineKeyboardButton(text="🗓 Отметки по дате", callback_data="otmetka_data_kb")],
            [InlineKeyboardButton(text="➕ Добавить группу", callback_data="add_group_kb"), InlineKeyboardButton(text="✏️ Редактировать профиль", callback_data="edit_profile_kb")]
]

start_kb = InlineKeyboardMarkup(inline_keyboard=start_kb)