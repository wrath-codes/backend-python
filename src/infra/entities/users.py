from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infra.config.db_base import Base


class Users(Base):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pets")

    def __repr__(self) -> str:
        return f"Usr [name={self.name}]"
