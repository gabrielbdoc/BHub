import re
from decimal import Decimal

from fastapi import HTTPException
from src.schemas.user_schemas import UserCreateInput, UserUpdateInput


class UserValidator:
    def is_user_data_valid(self, user_data: [UserCreateInput, UserUpdateInput]):
        try:
            if user_data.name:
                self.is_name_valid(user_data.name)
            if user_data.email:
                self.is_email_valid(user_data.email)
            if user_data.phone:
                self.is_phone_valid(user_data.phone)

        except Exception as error:
            raise HTTPException(400, str(error))

    @staticmethod
    def is_name_valid(name: str):
        pattern = "^([a-z A-Z]{0,100})+$"
        if not re.search(pattern, name):
            raise Exception("Invalid name.")

    @staticmethod
    def is_email_valid(email: str):
        pattern = "^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        if not re.search(pattern, email):
            raise Exception("Invalid email.")

    @staticmethod
    def is_phone_valid(email: str):
        pattern = "^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$"
        if not re.search(pattern, email):
            raise Exception("Invalid cellphone format. Please use '(xx) xxxxx-xxxx'")

    @staticmethod
    def format_income(income: Decimal):
        return "{:.2f}".format(income)
