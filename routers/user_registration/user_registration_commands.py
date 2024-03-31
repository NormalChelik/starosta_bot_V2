from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from texts.texts_user import (start_text,
                              start_registration_text,
                              input_full_name_text,
                              add_user_success_text)
from keyboards.user_kb.user_registration_commands_kb import create_groups_buttons
from db.sessions.session_user import (add_user,
                                      check_user)

from states.user_states import UserStates

user_registration_command_router = Router()

@user_registration_command_router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    check_u = check_user(user_id=message.from_user.id)
    if not check_u:
        await state.set_state(UserStates.input_group_state)
        await message.answer(text=start_registration_text, reply_markup=create_groups_buttons().as_markup(resize_keyboard=True))

    else:
        await message.answer(text=start_text.format(message.from_user.id,
                                                    message.from_user.username,
                                                    check_u[2],
                                                    check_u[1]))
@user_registration_command_router.message(UserStates.input_group_state)
async def input_group_state(message: Message, state: FSMContext):
    await message.answer(text=input_full_name_text)

    await state.update_data(input_group_state=message.text)
    await state.set_state(UserStates.input_full_name_state)

@user_registration_command_router.message(UserStates.input_full_name_state)
async def input_full_name_state(message: Message, state: FSMContext):
    await state.update_data(input_full_name_state=message.text)

    data = await state.get_data()
    add_user(
        user_id=message.from_user.id,
        group_name=data["input_group_state"],
        full_name=data["input_full_name_state"]
    )

    await message.answer(text=add_user_success_text.format(data["input_group_state"], data["input_full_name_state"]))

    await state.clear()
