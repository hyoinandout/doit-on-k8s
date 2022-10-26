import requests
from user_atom import MyAtom

my_atom = MyAtom(priority=100, cpu=250, mem=64)
print(my_atom.as_json())
response_create = requests.post("http://127.0.0.1:8000/api/v1/atoms", my_atom.as_json())
print(response_create)


