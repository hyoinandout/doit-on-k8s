import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'__dict__'):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)


def encode_whole_json(predeclared_dict:dict):
    return json.dumps(predeclared_dict, cls=ComplexEncoder).encode()