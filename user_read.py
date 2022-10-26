import requests

# response_read_all = requests.get("http://127.0.0.1:8000/api/v1/atoms")
# print(response_read_all.content)

# print()
response_read_one = requests.get(
    "http://127.0.0.1:8000/api/v1/atom/100-250-64-user_atom.MyAtom"
)
print(response_read_one.content)
