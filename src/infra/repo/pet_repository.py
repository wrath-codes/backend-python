# pylint: disable = E1101

from src.domain.models import Pets
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import Pets as PetModel


class PetRepository:
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
