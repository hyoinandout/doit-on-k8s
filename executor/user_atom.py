from atom import Atom, Requirements
import time


class MyAtom(Atom):
    def execute(self):
        print("Hello World")
        time.sleep(45)


# print(path.dirname(path.dirname(path.abspath(__file__))))
# sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
