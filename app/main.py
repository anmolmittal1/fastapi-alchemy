from fastapi import FastAPI

from app.apps.users import api as users_api

app = FastAPI()
app.include_router(users_api.router)
