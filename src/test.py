import unittest
from src.utils.user_validator import UserValidator


class TestUserValidator(unittest.TestCase):

    def test_is_name_valid(self):
        string = "Name Test"
        self.assertIsNone(UserValidator.is_name_valid(string))

    def test_is_name_invalid(self):
        string = "Name Test Error !!@"
        self.assertRaises(Exception, lambda: UserValidator.is_name_valid(string))

    def test_is_phone_valid(self):
        string = "(21) 97291-2123"
        self.assertIsNone(UserValidator.is_phone_valid(string))

    def test_is_phone_invalid(self):
        string = "Phone Teste Erro !!@"
        self.assertRaises(Exception, lambda: UserValidator.is_phone_valid(string))

    def test_is_email_valid(self):
        string = "test@mail.com"
        self.assertIsNone(UserValidator.is_email_valid(string))

    def test_is_email_invalid(self):
        string = "test@mail.com !@"
        self.assertRaises(Exception, lambda: UserValidator.is_email_valid(string))


if __name__ == '__main__':
    unittest.main()
