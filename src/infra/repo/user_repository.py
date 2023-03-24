from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.data.interfaces import IUserRepository
from src.domain.models import Users
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UserModel


class UserRepository(IUserRepository):
    """Class to manage User repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """Insert data in user entity
        :param - name: user name
        :param - password: user password
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserModel(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return Users(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_user(cls, id_user: int = None, name: str = None) -> List[Users]:
        """Select data in user entity by id or name
        :param - id_user: user's id
        :param - name: user's  name
        :return - list with Users selected
        """

        try:
            query_data = None

            if id_user and not name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(id=id_user)
                        .one()
                    )
                    query_data = [data]

            elif not id_user and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif id_user and name:
                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UserModel)
                        .filter_by(id=id_user, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []

        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

        return None
