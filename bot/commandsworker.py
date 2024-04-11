from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_bot_commands(bot: Bot):
    user_commands = [
        BotCommand(command="start", description="Перезапустить бот"),
        BotCommand(command="stats", description="Статистика по боту"),
        BotCommand(command="help", description="Справка"),
    ]
    await bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
