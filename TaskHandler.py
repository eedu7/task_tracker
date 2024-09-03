import json
# from pprint import pprint
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    IN_PROGRESS: str = "in-progress"
    TODO: str = "todo"
    DONE: str = "done"


class TaskHandler:
    def __init__(self, filename: str = "data.json", indent: int = 4):
        self.filename = filename
        self.indent = indent

    def add_task(self, task: str, description: str | None = None) -> str:
        task_id = self.__task_id()
        task_data: dict[str, str | None] = {
            "id": task_id,
            "task": task,
            "description": description,
            "status": TaskStatus.TODO.value,
            "createdAt": str(datetime.now()),
            "updatedAt": None,
        }
        data = self.__combine_data(task_data)
        self._create(data=data)
        return f"Task added successfully (ID: {task_id})"

    def view_task(self, filter_by: str = "", filter_value: str = ""):
        data = self._read()

        if not filter_by or not filter_value:
            return data

        return list(filter(lambda x: x[filter_by] == filter_value, data))

    def delete_task(self, task_id: str) -> str:
        data: list[dict] = self._read()
        task: list[dict] = self.view_task(filter_by="id", filter_value=task_id)[0]

        task_index: int = data.index(task)

        del data[task_index]

        self._create(data)

        return f"Task deleted successfully! (ID: {task_id})"

    def update_task(
        self,
        task_id: str,
        updated_task: str | None = None,
        updated_description: str | None = None,
    ) -> str:
        data = self._read()

        task_to_update = self.view_task(filter_by="id", filter_value=task_id)[0]
        ind: int = data.index(task_to_update)

        if updated_task:
            data[ind]["task"] = updated_task
        if updated_description:
            data[ind]["description"] = updated_description

        data[ind]["updatedAt"] = str(datetime.now())

        self._create(data)
        return f"Task updated successfully! (ID: {task_id})"

    def _read(self) -> list[dict]:
        try:
            with open(self.filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            self._create()
            return []
        except Exception as e:
            print(f"Error occurred while reading JSON file: {e}")

    def _create(self, data: dict[str, str] | list = []) -> None:
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=self.indent)
                return
        except Exception as e:
            print(f"Error occurred while creating JSON file: {e}")

    def __combine_data(self, new_data: dict) -> list[dict]:
        data = self._read()
        data.append(new_data)
        return data

    def __task_id(self) -> str:
        data = self._read()
        if data:
            return str(int(data[-1]["id"]) + 1)
        return "1"


if __name__ == "__main__":
    obj: TaskHandler = TaskHandler()

    obj.update_task(
        "6", updated_task="Update task", updated_description="updated_description"
    )
