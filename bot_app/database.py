from collections.abc import AsyncGenerator

import asyncpg

from bot_app.config import settings


class Database:
    def __init__(self):
        self._pool: asyncpg.Pool | None = None

    async def create_pool(self):
        if not self._pool:
            self._pool = await asyncpg.create_pool(
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_NAME,
                host=settings.DB_HOST,
                port=settings.DB_PORT,
                min_size=1,
                max_size=10,
            )

    async def close(self):
        if self._pool:
            await self._pool.close()

    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        if not self._pool:
            await self.create_pool()
        async with self._pool.acquire() as connection:
            yield connection


db = Database()


async def get_db_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    async for conn in db.get_connection():
        yield conn
