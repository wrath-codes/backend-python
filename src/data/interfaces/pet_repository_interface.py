from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Pets


class IPetRepository(ABC):
    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, id_user: int) -> Pets:
        """abstract method"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, id_user: int = None) -> List[Pets]:
        """abstract method"""
        raise Exception("Method not implemented")
