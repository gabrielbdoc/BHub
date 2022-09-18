from fastapi import HTTPException

from sqlalchemy import select, update, and_
from src.database.models import BankingData
from src.database.connection import async_session
from src.schemas.banking_data_schemas import BankingDataInput
from src.utils.assets import Assets
from src.services.user_services import UserService


class BankingDataService:

    @staticmethod
    async def create_banking_data(data: BankingDataInput):
        async with async_session() as session:
            if not await UserService.check_user_exists(data.user_id):
                raise HTTPException(404, "User Not Found")
            session.add(BankingData(bank_name=await Assets.get_bank_name(data.bank_code), bank_code=data.bank_code,
                                    bank_branch=data.bank_branch, account_id=data.account_id, user_id=data.user_id,
                                    created_at=Assets.timestamp()))
            await session.commit()

    async def list_bank_users(self, bank_code: int):
        async with async_session() as session:
            if not await self.check_bank_exists(bank_code):
                raise HTTPException(404, "Bank not found")
            result = await session.execute(select(BankingData).where(and_(
                BankingData.bank_code == bank_code,
                BankingData.deleted_at == None
            )))
            return result.scalars().all()

    async def delete_banking_data(self, data: BankingDataInput):
        async with async_session() as session:
            if not await UserService.check_user_exists(data.user_id):
                raise HTTPException(404, "Not Found")
            if not await self.check_banking_data_exists(data):
                raise HTTPException(404, "Incorrect banking data")
            data_dict = {
                "deleted_at": Assets.timestamp()
            }
            await session.execute(update(BankingData).where(and_(
                BankingData.deleted_at == None,
                BankingData.user_id == data.user_id,
                BankingData.bank_code == data.bank_code,
                BankingData.bank_branch == data.bank_branch,
                BankingData.account_id == data.account_id
            )).values(data_dict))
            await session.commit()

    @staticmethod
    async def check_banking_data_exists(data: BankingDataInput):
        async with async_session() as session:
            result = await session.execute(select(BankingData).where(and_(
                BankingData.deleted_at == None,
                BankingData.user_id == data.user_id,
                BankingData.bank_code == data.bank_code,
                BankingData.bank_branch == data.bank_branch,
                BankingData.account_id == data.account_id
            )))
            return result.scalars().all()

    @staticmethod
    async def check_bank_exists(bank_code: int):
        async with async_session() as session:
            result = await session.execute(select(BankingData).where(BankingData.bank_code == bank_code))
            return result.scalars().all()
