import asyncpg
from aiogram import Bot
from aiogram.filters import Command
from aiogram.filters.command import CommandObject
from aiogram.types import Message

from bot_app.api_clients.backend_public_api.models import (
    RegisterForTgNotifications,
    UserResponse,
)
from bot_app.api_connections.backend_api_functions import (
    register_user_for_notifications,
)
from bot_app.misc import aiogram_router


@aiogram_router.message(Command("start"))
async def handle_start(
    message: Message, command: CommandObject, bot: Bot, db: asyncpg.Connection
):
    if not command.args:
        await message.answer("Please provide a code.")
        return

    register_tg_notifications_payload = RegisterForTgNotifications(
        connection_code=command.args,
        tg_id=message.chat.id,
        tg_full_name=f"{message.from_user.first_name} {message.from_user.last_name}",
        tg_user_name=f"@{message.from_user.username}",
    )

    backend_user: UserResponse = await register_user_for_notifications(
        register_tg_notifications_payload
    )

    await message.answer(
        f"Hello! {backend_user.first_name} {backend_user.last_name}!\n Telegram notifications are connected now!"
    )
