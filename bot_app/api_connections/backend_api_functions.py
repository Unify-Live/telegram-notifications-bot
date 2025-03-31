from httpx import ConnectError

from bot_app.api_clients.backend_public_api import Client
from bot_app.api_clients.backend_public_api.api.telegram_notifications import (
    connect_telegram_notifications,
)
from bot_app.api_clients.backend_public_api.models import RegisterForTgNotifications
from bot_app.config import settings

# TODO implement normal error handling
backend_client = Client(settings.BACKEND_API_HOST)


async def register_user_for_notifications(
    registration_data: RegisterForTgNotifications,
):
    result = await connect_telegram_notifications.asyncio_detailed(
        client=backend_client, body=registration_data
    )
    if result.status_code != 200:
        raise ConnectError(message=result.content)
    return result.parsed
