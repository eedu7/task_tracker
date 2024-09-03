import datetime
import json
from enum import Enum
from pprint import pprint
from typing import Generator

FILE_NAME: str = "data.json"
ID_START: int = 0


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


def write_json(data: list[dict | None] = [], indent: int = 4) -> None:
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=indent)
    except Exception as e:
        print(f"Error occurred while writing JSON data from file: {e}")


def read_json() -> list[dict]:
    global ID_START
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            if data:
                ID_START = data[-1]["id"]
            return data
    except FileNotFoundError:
        print("File not found.\nCreating new file.")
        write_json()
        return []


def update_json(user_data: dict, data: list[dict]) -> dict:
    task_id = int(user_data[1])
    user_input: list = " ".join(user_data[2:])

    try:
        updated_task, updated_description = user_input.split('" "')
        updated_task, updated_description = (
            updated_task.replace('"', ""),
            updated_description.replace('"', ""),
        )
    except Exception:
        updated_task, updated_description = user_input, None
    try:
        json_obj = list(filter(lambda x: x["id"] == task_id, data))
        ind = data.index(json_obj[0])
        data[ind]["task"] = updated_task
        if updated_description is not None:
            data[ind]["description"] = updated_description
        write_json(data)
        print(f"Task updated successfully: (ID: {task_id})")

    except Exception as e:
        print("error ", e)


def update_status(task_id, status, data):
    json_obj = list(filter(lambda x: x["id"] == int(task_id), data))
    ind = data.index(json_obj[0])
    if "mark-in-progress" == status:
        data[ind]["status"] = Status.IN_PROGRESS.value
    elif "mark-done" == status:
        data[ind]["status"] = Status.DONE.value
    elif "mark-todo" == status:
        data[ind]["status"] = Status.TODO.value
    write_json(data)


def add_json(id: int, user_input: list[str], data: list) -> dict:
    user_input: list = " ".join(user_input[1:])
    try:
        user_input = user_input.split('" "')
        task, description = user_input[0], user_input[1]
    except Exception:
        task, description = str(user_input[0]).replace('"', ""), None

    new_task = {
        "id": id,
        "task": task,
        "status": Status.TODO.value,
        "description": description,
        "createdAT": str(datetime.datetime.now()),
        "updatedAT": None,
    }
    data.append(new_task)

    write_json(data)
    print(f"Task added successfully: (ID: {new_task.get('id')})")


def filter_data(user_input: list[str], data: list[dict]) -> list[dict]:
    if len(user_input) == 1:
        print(data)
        return
    try:
        filter_by = user_input[1]
        filter_data = [i for i in data if i["status"] == filter_by]
        pprint(filter_data)
    except Exception as e:
        print(f"Error occurred while filtering data: {e}")
        return


def generate_id() -> Generator:
    global ID_START
    i = ID_START
    while True:
        i += 1
        yield i


def delete_json(task_id: int, data: list[dict]) -> dict:
    task = [i for i in data if i["id"] == int(task_id)]
    if not task:
        print("Task not found.")
        return
    task_index = data.index(task[0])
    del data[task_index]
    write_json(data)
    print(f"Task with ID {task_id} deleted successfully.")


def main():
    id: Generator = generate_id()

    while True:
        data: list[dict] = read_json()
        user_input: list[str] = input("task-cli ").split(" ")

        match user_input[0]:
            case "add":
                new_id: int = next(id)
                if len(user_input) == 3 or len(user_input) == 4:
                    add_json(new_id, user_input, data)
                else:
                    print("Invalid input. Please provide task and description.")
            case "delete":
                delete_json(user_input[1], data)

            case "update":
                update_json(user_input, data)

            case "list":
                filter_data(user_input, data)

            case "mark-in-progress":
                update_status(user_input[1], "mark-in-progress", data)

            case "mark-done":
                update_status(user_input[1], "mark-done", data)

            case "mark-todo":
                update_status(user_input[1], "mark-todo", data)

            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
