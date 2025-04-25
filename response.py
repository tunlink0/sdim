import json
from dictobject import DictObject


def list_obj_to_dict(l: list[DictObject | list] | DictObject):
    if isinstance(l, DictObject):
        return l.to_dict()
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


def response_success_list(l: dict):
    return json.dumps({
        "_r": ResponseCode.OK,
        "_d": l
    })


def response_success_dict(l: dict):
    return json.dumps({
        "_r": ResponseCode.OK,
        "_d": l
    })


def response_error(code: int):
    return json.dumps({
        "_r": code,
    })
