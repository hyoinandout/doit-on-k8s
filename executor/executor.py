# import sys
import json
import importlib
import sys
import requests

# json_bytes = bytes(input(), encoding="utf-8")
# serialized = json.loads(json_bytes.decode("utf-8"))
json_bytes = eval(sys.argv[1][0] + "'" + sys.argv[1][1:] + "'")
serialized = json.loads(json_bytes.decode())

name = serialized["name"]
atom_id = serialized["atom_id"]
module_name, module_class_name = name.rsplit(".", 1)
module = importlib.import_module(module_name)
atom_cls = getattr(module, module_class_name)

new_atom = atom_cls.__new__(atom_cls)
new_atom.execute()

response_complete = requests.delete(
    f"http://doit-scheduler.default.svc.cluster.local:8000/api/v1/atom/{atom_id}"
)
# print(response_complete)
