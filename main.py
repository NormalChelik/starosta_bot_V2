import asyncio
import json

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers.admin_panel.admin_commands import admin_command_router
from routers.admin_panel.admin_callback import admin_callback_router

from routers.user_registration.user_registration_commands import user_registration_command_router

from db.create_db import create_tables

config_INFO = json.load(open("bot_config.json", "r"))

#Главная функция, запускает бота
async def main() -> None:
    bot = Bot(token=config_INFO["token"], parse_mode="Markdown")

    create_tables()

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(admin_command_router,
                       admin_callback_router,
                       user_registration_command_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())