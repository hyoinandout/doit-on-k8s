from atom import Atom, Requirements


class MyAtom(Atom):
    def __init__(
        self,
        priority: int,
        cpu: int,
        mem: int,
        name: str,
    ):
        self.priority = priority
        self.requirements = Requirements(cpu, mem)
        self.name = name
        self._id()

    def execute(self):
        print("Hello World")


# print(path.dirname(path.dirname(path.abspath(__file__))))
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
