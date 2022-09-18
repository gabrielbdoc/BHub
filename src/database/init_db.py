import platform

from asyncio import run, set_event_loop_policy, WindowsSelectorEventLoopPolicy

from src.database.connection import engine
from src.database.models import Base


async def create_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    run(create_database())
    print("Success")
