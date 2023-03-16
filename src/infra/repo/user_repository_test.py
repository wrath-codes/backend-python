from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UsersModel

from .user_repository import UserRepository

fake = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_user():
    """Should Insert User"""

    name = fake.name()
    password = fake.word()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_user = user_repository.insert_user(name, password)

    with engine.connect() as conn:
        query_user = conn.execute(
            text("SELECT * FROM users WHERE id = {}".format(new_user.id))
        ).fetchone()

    # Delete User
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users WHERE id = {}".format(new_user.id)))
        conn.commit()

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


def test_select_user():
    """Should select a user in Users table and compare it"""

    user_id = fake.random_number(digits=5)
    name = fake.name()
    password = fake.word()
    data = UsersModel(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()

    with engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO users (id, name, password) VALUES ({}, '{}', '{}')".format(
                    user_id, name, password
                )
            )
        )
        conn.commit()

    query_user1 = user_repository.select_user(user_id=user_id)
    query_user2 = user_repository.select_user(name=name)
    query_user3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in query_user1
    assert data in query_user2
    assert data in query_user3

    # Delete User
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM users WHERE id = {}".format(user_id)))
        conn.commit()
