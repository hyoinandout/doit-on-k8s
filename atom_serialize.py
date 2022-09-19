import json
from utils.utils import ComplexEncoder


if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path

        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from core.client.atom import Atom, Requirements
        from utils.utils import encode_whole_json

    class MyAtom(Atom):
        def __init__(
            self,
            priority: int,
            cpu: int,
            mem: int,
            name: str = "user_atom.MyAtom",
        ):
            self.priority = priority
            self.requirements = Requirements(cpu, mem)
            self.name = name
            self._id()

            # temp

        def execute(self):
            print("Hello World")

    my_atom1 = MyAtom(priority=123, cpu=250, mem=64)
    bstring = encode_whole_json(my_atom1.__dict__)
    print(json.dumps(bstring.decode(encoding="utf-8")))
