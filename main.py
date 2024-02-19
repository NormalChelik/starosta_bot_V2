import asyncio
import json

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers.admin_panel.admin_commands import admin_command_router

config_INFO = json.load(open("bot_config.json", "r"))

#Главная функция, запускает бота
async def main() -> None:
    bot = Bot(token=config_INFO["token"], parse_mode="Markdown")

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(admin_command_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())