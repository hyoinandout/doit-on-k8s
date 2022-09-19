import abc
import json
from utils.utils import ComplexEncoder


class Requirements:
    def __init__(self, cpu: int, mem: int):
        self.cpu = cpu
        self.mem = mem


class Atom(metaclass=abc.ABCMeta):
    atom_id: str
    priority: int
    requirements: Requirements
    name: str

    def _id(self):
        self.atom_id = str(
            str(self.priority)
            + "-"
            + str(self.requirements.cpu)
            + "-"
            + str(self.requirements.mem)
            + "-"
            + str(self.name)
        )

    @abc.abstractmethod
    def execute(self):
        pass

    def as_json(self):
        return json.dumps(self.__dict__, cls=ComplexEncoder)
