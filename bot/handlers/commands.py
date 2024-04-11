from aiogram import Router, types
from aiogram.filters import Command
from fluent.runtime import FluentLocalization

from services.user_service import UserService

router = Router()


@router.message(Command("help"))
async def help_command_handler(message: types.Message, l10n: FluentLocalization):
    await message.answer(l10n.format_value("help"))


@router.message(Command("stats"))
async def stats_command_handler(message: types.Message, l10n: FluentLocalization):
    user_count = await UserService().get_users_count()
    await message.answer(l10n.format_value("stats", args={"count": user_count}))
