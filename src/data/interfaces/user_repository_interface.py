from abc import ABC, abstractmethod
from typing import List

from src.domain.models import Users


class IUserRepository(ABC):
    @abstractmethod
    def insert_user(self, name: str, password: str) -> Users:
        """abstract method"""
        raise Exception("Method not implemented")

    @abstractmethod
    def select_user(self, user_id: int = None, name: str = None) -> List[Users]:
        """abstract method"""
        raise Exception("Method not implemented")
