from core.client.atom import Atom

class MyAtom(Atom):
    def __init__(self, priority: int, cpu: int, mem: int):
        super().__init__(priority, cpu, mem)