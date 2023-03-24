import enum

from sqlalchemy import Column, Enum, ForeignKey, Integer, String

from src.infra.config.db_base import Base


class AnimalTypes(enum.Enum):
    """Define Animal Types"""

    dog = "dog"
    cat = "cat"
    bird = "bird"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    specie = Column((Enum(AnimalTypes)), nullable=False)
    age = Column(Integer)
    id_user = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, id_user={self.id_user}]"

    def __eq__(self, other):
        if (
            self.id == other.id
            and self.name == other.name
            and self.specie == other.specie
            and self.age == other.age
            and self.id_user == other.id_user
        ):
            return True
        return False
