from pprint import pprint

from TaskHandler import TaskHandler, TaskStatus


def main():
    while True:
        task_obj: TaskHandler = TaskHandler()

        raw_input: str = input("task-cli: ").split()

        match raw_input[0]:
            case "list":
                if len(raw_input) == 1:
                    pprint(task_obj.view_task())

                elif raw_input[1] == "done":
                    pprint(task_obj.view_task(filter_by="status", filter_value="done"))
                elif raw_input[1] == "in-progress":
                    pprint(
                        task_obj.view_task(
                            filter_by="status", filter_value="in-progress"
                        )
                    )
                elif raw_input[1] == "todo":
                    pprint(task_obj.view_task(filter_by="status", filter_value="todo"))

            case "add":
                user_input = " ".join(raw_input[1:]).split('" "')
                task = user_input[0].replace('"', "")

                # if there is description
                if len(user_input) == 2:
                    description = user_input[1].replace('"', "")
                    response = task_obj.add_task(task, description)
                    print(response)
                    return

                response = task_obj.add_task(task)
                print(response)

            case "update":
                task_id = raw_input[1]
                if not task_id.isdigit():
                    print("Invalid id")
                    continue
                user_input = " ".join(raw_input[2:]).split('" "')
                updated_task = user_input[0].replace('"', "")

                if len(user_input) == 2:
                    updated_description = user_input[1].replace('"', "")
                    response = task_obj.update_task(
                        task_id, updated_task, updated_description
                    )

                else:
                    response = task_obj.update_task(task_id, updated_task)

                print(response)

            case "delete":
                task_id: str = raw_input[1]

                response = task_obj.delete_task(task_id)
                print(response)

            case "mark-in-progress":
                task_id: str = raw_input[1]
                response = task_obj.update_status(task_id, TaskStatus.IN_PROGRESS.value)
                print(response)
            case "mark-todo":
                task_id: str = raw_input[1]
                response = task_obj.update_status(task_id, TaskStatus.TODO.value)
                print(response)

            case "mark-done":
                task_id: str = raw_input[1]
                response = task_obj.update_status(task_id, TaskStatus.DONE.value)
                print(response)

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
