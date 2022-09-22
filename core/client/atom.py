import json
from utils.utils import ComplexEncoder


class Requirements:
    def __init__(self, cpu: int, mem: int):
        self.cpu = cpu
        self.mem = mem


class Atom:
    atom_id: str
    priority: int
    requirements: Requirements
    name: str  # 부모 클래스에서 아톰 이름을 정해줘야함

    def __init__(self, priority: int, cpu: int, mem: int):
        self.priority = priority
        self.requirements = Requirements(cpu, mem)
        self.atom_id = self._id()

    @property
    def name(self):
        return f"{self.__class__.__module__}.{self.__class__.__name__}"

    def _id(self):
        return str(
            str(self.priority)
            + "-"
            + str(self.requirements.cpu)
            + "-"
            + str(self.requirements.mem)
            + "-"
            + str(self.name)
        )

    def as_json(self):
        self.__dict__.update({"name": self.name})
        return json.dumps(self.__dict__, cls=ComplexEncoder)
