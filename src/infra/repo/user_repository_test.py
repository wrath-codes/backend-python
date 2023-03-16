from faker import Faker
from sqlalchemy import text

from src.infra.config import DBConnectionHandler

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
