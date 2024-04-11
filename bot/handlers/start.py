from aiogram import Router, types
from aiogram.filters import Command
from fluent.runtime import FluentLocalization

from services.user_service import UserService

router = Router()


@router.message(Command("start"))
async def start_message_handler(message: types.Message, l10n: FluentLocalization):
    if not await UserService.get_user(message.from_user.id):
        await UserService.create_user(message.from_user.id, message.from_user.first_name,
                                      message.from_user.last_name, message.from_user.username)
        await message.answer(l10n.format_value("registered"))
    await message.answer(l10n.format_value("start"))

