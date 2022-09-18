from typing import Optional

from pydantic import BaseModel


class BankingDataInput(BaseModel):
    user_id: int
    bank_code: int
    bank_name: Optional[str]
    bank_branch: int
    account_id: int


class BankingData(BaseModel):
    id: int
    user_id: int
    bank_name: str
    bank_code: int
    bank_branch: int
    account_id: int
    created_at: str
    deleted_at: Optional[str]

    class Config:
        orm_mode = True
