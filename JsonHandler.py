import json
from pprint import pprint


class JSONHandler:
    def __init__(self, filename: str = "data.json", indent: int = 4):
        self.filename = filename
        self.indent = indent

    def _read(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            self._create()
        except Exception as e:
            print(f"Error occurred while reading JSON file: {e}")

    def _create(self, data: dict[str, str] | list = []) -> None:
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=self.indent)
                return
        except Exception as e:
            print(f"Error occurred while creating JSON file: {e}")


if __name__ == "__main__":
    json_handler: JSONHandler = JSONHandler()

    pprint(json_handler)
