from faker import Faker

from src.domain.models import Users

fake = Faker()


def mock_users() -> Users:
    """Mocking Users"""
    return Users(
        id=fake.random_number(digits=5),
        name=fake.name(),
        password=fake.name(),
    )
