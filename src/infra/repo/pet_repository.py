# pylint: disable = E1101

from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.data.interfaces import IPetRepository
from src.domain.models import Pets
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import Pets as PetModel


class PetRepository(IPetRepository):
    """Class to manage Pet repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, age: int, id_user: int) -> Pets:
        """
        Insert data in PetsEntity entity
        :param - name: name of the pet
               - specie: specie of the pet
                - age: age of the pet
                - id_user: id of the user
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_conn:
            try:
                new_pet = PetModel(name=name, specie=specie, age=age, id_user=id_user)
                db_conn.session.add(new_pet)
                db_conn.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    id_user=new_pet.id_user,
                )
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()

        return None

    @classmethod
    def select_pet(cls, pet_id: int = None, id_user: int = None) -> List[Pets]:
        """
        Select data in PetsEntity entity
        :param - pet_id: id of the pet
               - id_user: id of the user
        :return - List with Pets selected
        """

        with DBConnectionHandler() as db_conn:
            try:
                query_data = None

                if pet_id and not id_user:
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(PetModel)
                            .filter_by(id=pet_id)
                            .one()
                        )
                        query_data = [data]

                elif not pet_id and id_user:
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(PetModel)
                            .filter_by(id_user=id_user)
                            .all()
                        )
                        query_data = data

                elif pet_id and id_user:
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(PetModel)
                            .filter_by(id=pet_id, id_user=id_user)
                            .one()
                        )
                        query_data = [data]

                return query_data

            except NoResultFound:
                return []
            except:
                db_conn.session.rollback()
                raise
            finally:
                db_conn.session.close()

            return None
