import asyncio
import json

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from texts.texts_admin import (start_text,
                               add_new_group_text,
                               input_add_new_group_text)
from keyboards.admin_kb.admin_commands_kb import start_kb
from states.admin_states import AdminStates

from db.sessions.session_admin import add_group

admin_callback_router = Router()
config_INFO = json.load(open("bot_config.json", "r"))

@admin_callback_router.callback_query(F.data == "add_group_kb", F.from_user.id.in_({config_INFO["admin_id"]}))
async def add_group(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(AdminStates.add_group_state)
    await clbck.message.edit_text(text=add_new_group_text)

@admin_callback_router.message(AdminStates.add_group_state, F.from_user.id.in_({config_INFO["admin_id"]}))
async def input_add_group(message: Message, state: FSMContext):
    add_group(group_name=message.text)
    mess = await message.answer(text=input_add_new_group_text.format(message.text, 1))

    await state.update_data(add_new_group_text=message.text)

    for i in range(2, 6):
        await asyncio.sleep(1)
        await mess.edit_text(text=input_add_new_group_text.format(message.text, i))

    await mess.edit_text(text=start_text.format(message.from_user.id, message.from_user.username, "БОСО-01-23", "labuchov.r.f@edu.mirea.ru"),
                         reply_markup=start_kb)

    await state.clear()


