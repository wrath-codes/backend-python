from faker import Faker
from sqlalchemy import text

from src.domain.models.pets import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities.pets import AnimalTypes

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


def test_select_pet():
    """Should select a pet in Pets table and compare it"""

    pet_id = fake.random_number(digits=4)
    name = fake.name()
    specie = "fish"
    age = fake.random_number(digits=1)
    id_user = fake.random_number()

    engine = db_connection_handler.get_engine()

    specie_mock = AnimalTypes("fish")
    data = Pets(id=pet_id, name=name, specie=specie_mock, age=age, id_user=id_user)

    # SQL Commands
    with engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO pets (id, name, specie, age, id_user) VALUES ({}, '{}', '{}', {}, {});".format(
                    pet_id, name, specie, age, id_user
                )
            )
        )
        conn.commit()

    query_pets1 = pet_repository.select_pet(pet_id=pet_id)
    query_pets2 = pet_repository.select_pet(id_user=id_user)
    query_pets3 = pet_repository.select_pet(pet_id=pet_id, id_user=id_user)

    assert data in query_pets1
    assert data in query_pets2
    assert data in query_pets3

    # Delete Pet
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM pets WHERE id = {}".format(pet_id)))
        conn.commit()
