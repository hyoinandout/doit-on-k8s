import requests
from core.client.atom import Atom, Requirements


class MyAtom(Atom):
    def __init__(self, priority: int, cpu: int, mem: int, name: str):
        self.priority = priority
        self.requirements = Requirements(cpu, mem)
        self.name = name
        self._id()

    def execute(self):
        print("Hello World")

my_atom = MyAtom(priority=123, cpu=250, mem=64,name="user_atom.MyAtom")
print(my_atom.as_json())
response_create = requests.post("http://127.0.0.1:8000/api/v1/atoms", my_atom.as_json())
print(response_create)
