import json
from .file_list import FileList
from .list import convert as convert_list


def convert(file: str, model: str, custom_pk: str = None) -> FileList:
    with open(file) as f:
        data = json.load(f)

    return convert_list(data, model, custom_pk)
