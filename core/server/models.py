from sqlalchemy import Column, String, Integer
from .database import Base


class Atom(Base):
    __tablename__ = "atoms"

    id = Column(Integer, autoincrement=True, primary_key=True)
    atom_id = Column(String)
    status = Column(String)
    