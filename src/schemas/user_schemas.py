from typing import List, Optional

from pydantic import BaseModel
from decimal import Decimal

from src.schemas.banking_data_schemas import BankingData


class UserCreateInput(BaseModel):
    name: str
    phone: str
    address: str
    income: Decimal
    email: str


class UserUpdateInput(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    income: Optional[Decimal]
    email: Optional[str]


class UserDeleteInput(BaseModel):
    user_id: int


class UserReadOutput(BaseModel):
    name: str
    phone: str
    address: str
    income: Decimal


class UserListOutput(BaseModel):
    id: int
    name: str
    phone: str
    address: Optional[str]
    income: Decimal
    email: Optional[str]
    created_at: str
    updated_at: Optional[str]
    deleted_at: Optional[str]
    banking_data: List[BankingData]

    class Config:
        orm_mode = True
