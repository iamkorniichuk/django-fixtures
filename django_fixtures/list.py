from typing import Dict, Iterable
from .file_list import FileList


def convert(data: Iterable[Dict], model: str, custom_pk: str = None) -> FileList:
    results = FileList([])
    for pk, row in enumerate(data, 1):
        if custom_pk:
            pk = row.pop(custom_pk)
        results.append({"model": model, "pk": pk, "fields": row})
    return results
