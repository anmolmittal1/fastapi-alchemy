from typing import Any, AsyncGenerator
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from . import models as users_models
from . import schema as users_schema


class UserManager:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(
        self, user: users_schema.User
    ) -> AsyncGenerator[users_models.User, Any]:
        async with self.session.begin():
            return await self.session.scalar(
                insert(users_models.User).returning(users_models.User), [user.dict()]
            )
