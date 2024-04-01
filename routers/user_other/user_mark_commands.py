import asyncio
import datetime
import json

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from api.normal import (get_schedule)

user_mark_command_router = Router()

async def check_schedule(login: str, password: str):
    global lessons

    while True:
        with open("bot_config.json", "r") as config:
            config_INFO = json.load(config)

            config_INFO["date_today"] = datetime.datetime.now()

        if datetime.datetime.now().strftime("%H:%M:%S") == "00:00:00":
            lessons = get_schedule(login=login,
                                   password=password)

        await asyncio.sleep(300)
async def create_mark():


    while True:
        get_schedule()