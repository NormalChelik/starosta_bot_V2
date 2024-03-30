from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from db.sessions.session_user import check_groups

def create_groups_buttons():
    check_groups()
    groups = check_groups()

    groups_bts = ReplyKeyboardBuilder()

    for group in groups:
        groups_bts.add(KeyboardButton(text=group[0]))
    groups_bts.adjust(3)

    return groups_bts