import requests

response_delete = requests.delete("http://127.0.0.1:8000/api/v1/atom/123-250-64-user_atom.MyAtom")
print(response_delete)
