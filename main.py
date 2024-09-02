import json
from pprint import pprint

FILE_NAME: str = "data.json"

def write_json(data: list[dict | None] = [], indent: int = 4) -> None:
    try:
        print("Writing JSON data")
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=indent, )
        print("Success!")
    except Exception as e:
        print(f"Error occurred while writing JSON data from file: {e}")


def read_json() -> list[dict]:
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.\nCreating new file.")
        write_json()
        return []


def update_json(user_data: dict, data: list[dict]) -> dict: ...


def delete_json(task_id: int, data: list[dict]) -> dict: ...


def add_json(user_data: dict, data: dict) -> dict:
    new_data = data.copy()
    new_data.append(user_data)
    pprint(new_data)
    with open(FILE_NAME, "w") as file:
        json.dump(new_data, file)
    


def main():
    data = read_json()
    user_data: dict[str, str] = {"id": "1", "task": "John"}
    add_json(user_data, data)
    


if __name__ == "__main__":
    main()
