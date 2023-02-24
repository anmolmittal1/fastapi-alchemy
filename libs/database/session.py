from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost:5432/appdb", echo=True
)
AsyncDBSession = async_sessionmaker(engine, expire_on_commit=False)
