from typing import Any

from pandas import array
from faker import Faker
from uuid import uuid4

fake = Faker()

def generate_one() -> any:
    
    user = {
        "_id": uuid4(),
        "fullname": fake.name(),
        "country": fake.country(),
        "address": fake.address()
    }

    return user

def generate(count: int) -> array:
    users = []
    for i in range(count):
        users.append(generate_one())

    return users

