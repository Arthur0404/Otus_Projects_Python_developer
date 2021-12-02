"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession
import asyncio

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data():
    async with ClientSession() as session:
        async with session.get(USERS_DATA_URL) as users_data:
            return await users_data.json()


async def fetch_posts_data():
    async with ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as post_data:
            return await post_data.json()
