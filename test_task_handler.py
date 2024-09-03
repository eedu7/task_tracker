import os
import unittest
from datetime import datetime

from TaskHandler import TaskHandler


class TestClass(unittest.TestCase):
    def setUp(self):
        self.filename = "test.json"
        self.obj = TaskHandler(filename=self.filename)

    def test_create_empty_json(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

        self.obj._create()

        self.assertTrue(os.path.isfile(self.filename))

    def test_create_data_json(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

        dummy_data: list[dict] = [
            {
                "id": "1",
                "task": "Test Task",
                "description": "Test Task Description",
                "status": "todo",
                "createdAT": str(datetime.now()),
                "updatedAt": None,
            }
        ]

        self.obj._create(data=dummy_data)

        self.assertTrue(os.path.isfile(self.filename))

    def test_read_json(self):
        data = self.obj._read()
        self.assertIsInstance(data, list)
        self.assertEqual(data, [])

    def test_read_json_no_existing_file(self):
        self.new_obj = TaskHandler(filename="no.json")
        data = self.obj._read()
        self.assertIsInstance(data, list)
        self.assertEqual(data, [])

    def test_read_data_json(self):
        dummy_data: list[dict] = [
            {
                "id": "1",
                "task": "Test Task",
                "description": "Test Task Description",
                "status": "todo",
                "createdAT": str(datetime.now()),
                "updatedAt": None,
            }
        ]

        self.obj._create(data=dummy_data)

        data = self.obj._read()

        self.assertEqual(data, dummy_data)

    def test_add_task_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["task"], task)
        self.assertEqual(last_task["description"], description)
        self.assertEqual(last_task["status"], "todo")
        self.assertIsNotNone(last_task["id"])
        self.assertIsNotNone(last_task["createdAt"])
        self.assertIsNotNone(last_task["status"])

    def test_add_without_description_json(self):
        task = "Dummy Task without any description"

        self.obj.add_task(task=task)

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["task"], task)
        self.assertEqual(last_task["status"], "todo")
        self.assertIsNotNone(last_task["id"])
        self.assertIsNotNone(last_task["createdAt"])
        self.assertIsNotNone(last_task["createdAt"])

    def test_update_task_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        updated_task = "Updated Dummy Task"
        self.obj.update_task(lastest_task_id, updated_task)

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["id"], lastest_task_id)
        self.assertEqual(last_task["task"], updated_task)
        self.assertEqual(last_task["description"], description)

    def test_update_description_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        updated_description = "Updated Dummy Task Description"
        self.obj.update_task(lastest_task_id, updated_description=updated_description)

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["id"], lastest_task_id)
        self.assertEqual(last_task["task"], task)
        self.assertEqual(last_task["description"], updated_description)

    def test_update_task_and_description_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        updated_task = "Updated Dummy Task"
        updated_description = "Updated Dummy Task Description"
        self.obj.update_task(lastest_task_id, updated_task, updated_description)

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["id"], lastest_task_id)
        self.assertEqual(last_task["task"], updated_task)
        self.assertEqual(last_task["description"], updated_description)

    def test_update_status_in_progress_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        self.obj.update_status(lastest_task_id, "in-progress")

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["status"], "in-progress")

    def test_update_status_done_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        self.obj.update_status(lastest_task_id, "done")

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["status"], "done")

    def test_update_status_todo_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        self.obj.update_status(lastest_task_id, "todo")

        data = self.obj._read()

        last_task = data[-1]

        self.assertEqual(last_task["status"], "todo")

    def test_delete_json(self):
        task = "Dummy Task with description"
        description = "Dummy Task with Description"

        self.obj.add_task(task=task, description=description)

        data = self.obj._read()

        last_task = data[-1]

        task_id = last_task["id"]

        self.obj.delete_task(task_id)

        data = self.obj._read()
        self.assertEqual(data, [])

    def test_list_json(self):
        task_1 = "Dummy Task 1"
        description_1 = "Dummy Task 1 Description"

        self.obj.add_task(task=task_1, description=description_1)
        task_2 = "Dummy Task 2"
        description_2 = "Dummy Task 2 Description"

        self.obj.add_task(task=task_2, description=description_2)

        data = self.obj.view_task()

        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["task"], task_1)
        self.assertEqual(data[0]["description"], description_1)
        self.assertEqual(data[1]["task"], task_2)
        self.assertEqual(data[1]["description"], description_2)

    def test_list_in_progress_json(self):
        task_1 = "Dummy Task 1"
        description_1 = "Dummy Task 1 Description"

        self.obj.add_task(task=task_1, description=description_1)
        task_2 = "Dummy Task 2"
        description_2 = "Dummy Task 2 Description"

        self.obj.add_task(task=task_2, description=description_2)

        data = self.obj.view_task()

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        self.obj.update_status(lastest_task_id, "in-progress")

        response = self.obj.view_task(filter_by="status", filter_value="in-progress")

        self.assertEqual(response[0]["status"], "in-progress")

    def test_list_todo_json(self):
        task_1 = "Dummy Task 1"
        description_1 = "Dummy Task 1 Description"

        self.obj.add_task(task=task_1, description=description_1)
        task_2 = "Dummy Task 2"
        description_2 = "Dummy Task 2 Description"

        self.obj.add_task(task=task_2, description=description_2)

        response = self.obj.view_task(filter_by="status", filter_value="todo")

        self.assertEqual(response[0]["status"], "todo")

    def test_list_done_json(self):
        task_1 = "Dummy Task 1"
        description_1 = "Dummy Task 1 Description"

        self.obj.add_task(task=task_1, description=description_1)
        task_2 = "Dummy Task 2"
        description_2 = "Dummy Task 2 Description"

        self.obj.add_task(task=task_2, description=description_2)

        data = self.obj.view_task()

        data = self.obj._read()

        last_task = data[-1]

        lastest_task_id = last_task["id"]
        self.obj.update_status(lastest_task_id, "done")

        response = self.obj.view_task(filter_by="status", filter_value="done")

        self.assertEqual(response[0]["status"], "done")

    def tearDown(self):
        # Removing the json file after the test
        if os.path.isfile(self.filename):
            os.remove(self.filename)


if __name__ == "__main__":
    unittest.main()
