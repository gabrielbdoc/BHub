from datetime import datetime

from aiohttp import ClientSession
from fastapi import HTTPException

from src.settings import BANKING_INFO_PATH


class Assets:

    @staticmethod
    def timestamp() -> str:
        return str(datetime.now())

    @staticmethod
    async def get_bank_name(code: int) -> str:
        try:
            async with ClientSession() as session:
                response = await session.get(BANKING_INFO_PATH+f'{str(code)}')
                data = await response.json()
                return data["fullName"]
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))
