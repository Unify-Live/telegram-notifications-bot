from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import TokenBasedRequestHandler

from bot_app.config import settings

aiogram_router = Router()

# TODO think about local bot api?
session = AiohttpSession()
bot_settings = {"session": session, "default": DefaultBotProperties(parse_mode="HTML")}

# TODO think about redis if we will need any states at all?
storage = MemoryStorage()
bot = Bot(settings.TELEGRAM_BOT_TOKEN, **bot_settings)
# Create dispatcher for handling multiple bots
multibot_dispatcher = Dispatcher(storage=storage)
multibot_dispatcher.include_router(aiogram_router)

# Register handler for processing updates from different bots
webhook_handler = TokenBasedRequestHandler(
    dispatcher=multibot_dispatcher,
    bot_settings=bot_settings,
)
