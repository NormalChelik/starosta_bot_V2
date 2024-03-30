import json

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

from texts.texts_user import start_text
from keyboards.user_kb.user_registration_commands_kb import create_groups_buttons

user_registration_command_router = Router()

@user_registration_command_router.message(Command("start"))
async def start(message: Message):
    await message.answer(text=start_text, reply_markup=create_groups_buttons().as_markup(resize_keyboard=True))