import asyncio
import logging

from aiogram import Bot, Dispatcher
from fluent.runtime import FluentLocalization, FluentResourceLoader
from pathlib import Path

from config import BOT_TOKEN
from db.create_tables import init_database
from middlewares import L10nMiddleware
from commandsworker import set_bot_commands
from handlers import start, commands, message


async def main():
    await init_database()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    locales_dir = Path(__file__).parent.joinpath("locales")
    l10n_loader = FluentResourceLoader(str(locales_dir) + "/{locale}")
    l10n = FluentLocalization(["ru"], ["strings.ftl"], l10n_loader)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(start.router, commands.router, message.router)

    dp.update.middleware(L10nMiddleware(l10n))

    await set_bot_commands(bot)
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


asyncio.run(main())