# Setup
```
docker compose up -d
pipenv sync
pipenv shell
alembic upgrade head
uvicorn app.main:app --reload
```
