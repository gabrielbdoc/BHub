from fastapi import HTTPException
from sqlalchemy import select, update, and_

from src.database.models import User, BankingData
from src.database.connection import async_session
from src.schemas.user_schemas import UserCreateInput, UserUpdateInput
from src.utils.user_validator import UserValidator
from src.utils.assets import Assets


class UserService:

    @staticmethod
    async def create_user(data: UserCreateInput):
        async with async_session() as session:
            session.add(User(name=data.name, income=UserValidator.format_income(data.income),
                             created_at=Assets.timestamp(), address=data.address, phone=data.phone, email=data.email))
            await session.commit()

    async def delete_user(self, user_id: int):
        async with async_session() as session:
            if not await self.check_user_exists(user_id):
                raise HTTPException(404, "Not Found")
            data_dict = {
                "deleted_at": Assets.timestamp()
            }
            await session.execute(update(BankingData).where(BankingData.user_id == user_id).values(data_dict))
            await session.execute(update(User).where(User.id == user_id).values(data_dict))
            await session.commit()

    @staticmethod
    async def list_user(user_id):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            return result.scalars().all()

    @staticmethod
    async def list_users():
        async with async_session() as session:
            result = await session.execute(select(User).where(and_(
                User.deleted_at == None,
                # BankingData.deleted_at == None
            )))
            return result.scalars().all()

    @staticmethod
    async def check_user_exists(user_id: int):
        async with async_session() as session:
            result = await session.execute(select(User).where(and_(User.deleted_at == None, User.id == user_id)))
            return result.scalars().all()

    async def update_user(self, user_id: int, user_data: UserUpdateInput):
        async with async_session() as session:
            if not await self.check_user_exists(user_id):
                raise HTTPException(404, "Not Found")
            user_data_dict = user_data.dict(exclude_unset=True)
            user_data_dict["updated_at"] = Assets.timestamp()
            await session.execute(update(User).where(User.id == user_id).values(user_data_dict))
            await session.commit()
