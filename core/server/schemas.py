from pydantic import BaseModel


class Requirements(BaseModel):
    cpu: int
    mem: int


class AtomBase(BaseModel):
    atom_id: str
    status: str = "queued"

    class Config:
        orm_mode = True


class Atom(AtomBase):
    requirements: Requirements
    name: str
    priority: int
