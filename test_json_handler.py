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
        self.assertIsNone(data)

    def test_read_json_no_existing_file(self):
        self.new_obj = TaskHandler(filename="no.json")
        data = self.obj._read()
        self.assertIsNone(data)

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

    # def test_add_task_json(self): ...

    # def test_add_with_description_json(self): ...

    # def test_update_task_json(self): ...

    # def test_update_description_json(self): ...

    # def test_update_task_and_description_json(self): ...

    # def test_update_status_json(self): ...

    # def test_update_status_in_progress_json(self): ...
    # def test_update_status_done_json(self): ...
    # def test_update_status_todo_json(self): ...

    # def test_delete_json(self): ...

    # def test_list_json(self): ...

    # def test_list_in_progress_json(self): ...

    # def test_list_todo_json(self): ...

    # def test_list_done_json(self): ...

    def tearDown(self):
        # Removing the json file after the test
        if os.path.isfile(self.filename):
            os.remove(self.filename)


if __name__ == "__main__":
    unittest.main()
