# from typing import Optional

# import asyncpg

# from bot_app.schemas.bot_settings import BotResponse, NewBotRequest


# async def save_bot(db: asyncpg.Connection, new_bot_data: NewBotRequest) -> BotResponse:
#     query = "INSERT INTO bot (uuid, integration_uuid, api_key, api_secret, bot_token) VALUES ($1, $2, $3, $4, $5)"
#     params = (
#         new_bot_data.uuid,
#         new_bot_data.integration_uuid,
#         new_bot_data.api_key,
#         new_bot_data.api_secret,
#         new_bot_data.bot_token,
#     )
#     await db.execute(query, *params)
#     return BotResponse(
#         uuid=new_bot_data.uuid,
#         integration_uuid=new_bot_data.integration_uuid,
#         api_key=new_bot_data.api_key,
#         api_secret=new_bot_data.api_secret,
#         bot_token=new_bot_data.bot_token,
#     )


# async def get_bot_by_integration_uuid(
#     db: asyncpg.Connection, integration_uuid: str
# ) -> Optional[BotResponse]:
#     query = "SELECT uuid, integration_uuid, api_key, api_secret, bot_token FROM bot WHERE integration_uuid = $1"
#     bot = await db.fetchrow(query, integration_uuid)
#     if not bot:
#         return None
#     return BotResponse(**bot)


# async def get_bot_by_uuid(db: asyncpg.Connection, uuid: str) -> Optional[BotResponse]:
#     query = "SELECT uuid, integration_uuid, api_key, api_secret, bot_token FROM bot WHERE uuid = $1"
#     bot = await db.fetchrow(query, uuid)
#     if not bot:
#         return None
#     return BotResponse(**bot)
