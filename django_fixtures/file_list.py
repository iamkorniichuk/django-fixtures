import json


class FileList(list):
    def save_to_json(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self, f, ensure_ascii=False, indent=4)
