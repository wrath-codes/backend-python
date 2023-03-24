from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.models import Pets


class FindPet(ABC):
    """Interface to Find Pet use case"""

    @abstractmethod
    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """Abstract method to find a pet"""
        raise NotImplementedError("Should implement method: by_pet_id")

    @abstractmethod
    def by_user_id(self, id_user: int) -> Dict[bool, List[Pets]]:
        """Abstract method to find a pet"""
        raise NotImplementedError("Should implement method: by_user_id")

    @abstractmethod
    def by_pet_id_and_user_id(
        self, pet_id: int, id_user: int
    ) -> Dict[bool, List[Pets]]:
        """Abstract method to find a pet"""
        raise NotImplementedError("Should implement method: by_pet_id_and_user_id")
