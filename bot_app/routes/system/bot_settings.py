from typing import Annotated

import asyncpg
from aiogram import types
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramForbiddenError,
)
from fastapi import APIRouter, Depends, Header, HTTPException, status

from bot_app.config import settings
from bot_app.database import get_db_connection
from bot_app.misc import bot, multibot_dispatcher
from bot_app.schemas.messages import NewNotification

root_router = APIRouter(
    prefix="",
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@root_router.post(
    "/new-notification/",
    operation_id="new_notification",
    description="Endpoint to consume new notification from backend",
)
async def new_notification(
    new_notification: NewNotification,
) -> dict:
    try:
        await bot.send_message(
            chat_id=new_notification.tg_chat_id,
            text=new_notification.content,
        )
    except TelegramBadRequest as e:
        if "bot was kicked from the group chat" in e.message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="bot was kicked from the group chat",
            )
        if "chat not found" in e.message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="chat not found",
            )
        else:
            raise Exception from e
    except TelegramForbiddenError as e:
        if "blocked by the user" not in e.message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="blocked by the user"
            )
        else:
            raise Exception from e
    return {}


@root_router.post("/bot-webhook/", operation_id="bot_webhook")
async def bot_webhook(
    update: dict,
    x_telegram_bot_api_secret_token: Annotated[str | None, Header()] = None,
    db: asyncpg.Connection = Depends(get_db_connection),
):
    if x_telegram_bot_api_secret_token != settings.TELEGRAM_API_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )

    telegram_update = types.Update(**update)
    try:
        await multibot_dispatcher.feed_raw_update(
            bot=bot,
            update=telegram_update,
            db=db,
        )
    finally:
        # We are returning 200 here because telegram API does not care about our side of processing update
        # We only should let them now we have processed it even if we failed
        return {}
