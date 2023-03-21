from faker import Faker

from src.domain.models import Pets

fake = Faker()


def mock_pet() -> Pets:
    """Mocking Pet
    :param - None
    :return - Fake Pet registry
    """

    return Pets(
        id=fake.random_number(digits=5),
        name=fake.name(),
        specie="dog",
        age=fake.random_number(digits=1),
        id_user=fake.random_number(digits=5),
    )
