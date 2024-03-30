import json

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command

from texts.texts_admin import (start_text)
from keyboards.admin_kb.admin_commands_kb import (start_kb)

admin_command_router = Router()
config_INFO = json.load(open("bot_config.json", "r"))

@admin_command_router.message(Command("admin"), F.from_user.id.in_({config_INFO["admin_id"]}))
async def start(message: Message):
    await message.answer(text=start_text.format(message.from_user.id, message.from_user.username, "БОСО-01-23", "labuchov.r.f@edu.mirea.ru"),
                         reply_markup=start_kb)