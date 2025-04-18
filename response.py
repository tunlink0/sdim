import json
from dictobject import DictObject

def list_obj_to_dict(l: list[DictObject | list]):
    out = []
    for i in l:
        if isinstance(i, list):
            out.append(list_obj_to_dict(i))
        else:
            out.append(i.to_dict())

    return out


class ResponseCode:
    OK = 200
    NotFound = 404,


def response_success_list(l: list[object | list]):
    return json.dumps({
        "_r": ResponseCode.OK,
        "_d": list_obj_to_dict(l)
    })

def response_error(code: int):
    return json.dumps({
        "_r": code,
    })
