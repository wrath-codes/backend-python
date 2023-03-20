from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler

from .pet_repository import PetRepository

db_connection_handler = DBConnectionHandler()

fake = Faker()
pet_repository = PetRepository()


def test_insert_test():
    """Should insert a test in test table and return it"""

    name = fake.name()
    specie = "fish"
    age = fake.random_number(digits=1)
    user_id = fake.random_number()

    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_pet = pet_repository.insert_pet(name, specie, age, user_id)

    with engine.connect() as conn:
        query_pet = conn.execute(
            text("SELECT * FROM pets WHERE id = {}".format(new_pet.id))
        ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.id_user == query_pet.id_user

    # Delete Pet
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM pets WHERE id = {}".format(new_pet.id)))
        conn.commit()
