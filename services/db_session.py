import os
from contextlib import asynccontextmanager
from psycopg_pool import AsyncConnectionPool
from psycopg.rows import dict_row


# Construct the database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create an asynchronous connection pool
pool = AsyncConnectionPool(DATABASE_URL, min_size=1, max_size=20)

@asynccontextmanager
async def get_db_connection():
    async with pool.connection() as conn:
        yield conn

@asynccontextmanager
async def get_db_cursor():
    async with pool.connection() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            yield cur

async def execute_query(query, params=None):
    async with get_db_cursor() as cursor:
        await cursor.execute(query, params)
        return await cursor.fetchall()

async def execute_transaction(queries):
    async with get_db_connection() as conn:
        async with conn.transaction():
            for query, params in queries:
                await conn.execute(query, params)
