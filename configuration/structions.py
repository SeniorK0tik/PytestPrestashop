import pathlib
import random
from datetime import date
from enum import Enum
from typing import Optional

from faker import Faker
from pydantic import SecretStr
from pydantic.dataclasses import dataclass


root_dir: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent


class SocialTitle(str, Enum):
    MR = 'Mr.'
    Mrs = 'Mrs.'


@dataclass
class User:
    """Base class for Prestashop user"""
    social_title: SocialTitle
    first_name: str
    last_name: str
    email: str
    password: SecretStr
    birthday: Optional[date]

    def __str__(self):
        return f"First_name: {self.first_name}, Last_name: {self.last_name}, Email: {self.email}," \
               f" Password: {self.password}, Birthday: {self.birthday}"

    class Config:
        allow_population_by_field_name = True

    @classmethod
    def get_random(cls) -> 'User':
        """
        The function `get_random` returns a randomly generated instance of the `User` class.

        :param cls: The `cls` parameter in a class method refers to the class itself. It is used to access class-level
        attributes and methods
        :return: The method is returning an instance of the User class.
        """
        fake = Faker()
        return User(
            social_title=random.choice(list(SocialTitle)),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password=fake.password(length=10),
            birthday=fake.date_of_birth()
        )


if __name__ == '__main__':
    f = User.get_random()
