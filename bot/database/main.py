from os import getenv

import asyncpg


async def connect_db() -> asyncpg.Connection:
    connection = await asyncpg.connect(
        user=getenv('DB_USER'),
        password=getenv('DB_PASSWORD'),
        database=getenv('DB_NAME'),
        host=getenv('DB_HOST')
        )

    return connection

