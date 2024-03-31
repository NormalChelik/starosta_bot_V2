from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    input_group_state = State()
    input_full_name_state = State()