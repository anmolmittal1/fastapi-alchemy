from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import deps as common_deps

from . import managers as users_managers
from . import schema as users_schema

router = APIRouter(prefix="/users")


@router.post("")
async def create_user(
    user_data: users_schema.User,
    db_session: AsyncSession = Depends(common_deps.get_session),
) -> users_schema.User:
    return await users_managers.UserManager(db_session).create(user_data)
