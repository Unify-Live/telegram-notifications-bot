from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bot_app.config import settings
from bot_app.database import db
from bot_app.misc import bot
from bot_app.routes.system.bot_settings import root_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.create_pool()
    await bot.delete_webhook()
    print(f"Webhook: {settings.WEBHOOK_HOST}/bot-webhook/")
    await bot.set_webhook(
        url=f"{settings.WEBHOOK_HOST}/bot-webhook/",
        secret_token=settings.TELEGRAM_API_SECRET,
    )
    yield
    await db.close()


app = FastAPI(
    lifespan=lifespan,
    docs_url="/",
    version=settings.VERSION,
    swagger_ui_parameters={"syntaxHighlight": False},
    root_path=settings.FASTAPI_BASE_PATH,
    title="Bot Integration API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_ADDRESS, port=int(settings.SERVER_PORT))
