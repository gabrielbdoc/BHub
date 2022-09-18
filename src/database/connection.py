import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)


engine = create_async_engine("postgresql+asyncpg://bhub:bhub123!@localhost:5432/bhub")
async_session = sessionmaker(engine, class_=AsyncSession)
