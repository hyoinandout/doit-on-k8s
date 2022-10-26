from core.client.atom import Atom
import time

class MyAtom(Atom):
    def __init__(self, priority: int, cpu: int, mem: int):
        super().__init__(priority, cpu, mem)

    def execute(self):
        print("Hello World")
        time.sleep(45)
