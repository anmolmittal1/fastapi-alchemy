import asyncio
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from libs.database import AsyncDBSession


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncDBSession()
    try:
        yield session
    finally:
        task = asyncio.create_task(session.close())
        await asyncio.shield(task)
