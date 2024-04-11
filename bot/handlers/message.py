from aiogram import Router, types
from fluent.runtime import FluentLocalization


router = Router()


@router.message()
async def repeat_handler(message: types.Message):
    await message.answer(message.text)

