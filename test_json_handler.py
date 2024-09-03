import os
import unittest
from datetime import datetime

from JsonHandler import JSONHandler


class TestClass(unittest.TestCase):
    def setUp(self):
        self.filename = "test.json"
        self.obj = JSONHandler(filename=self.filename)

    def test_create_empty_json(self):
        # Checking if the file exists
        if os.path.isfile(self.filename):
            os.remove(self.filename)

        # creating the file
        self.obj._create()

        # Checking if the file is created
        self.assertTrue(os.path.isfile(self.filename))

    def test_create_data_json(self):
        # Checking if the file exists
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

        # creating the file
        self.obj._create(data=dummy_data)

        # Checking if the file is created
        self.assertTrue(os.path.isfile(self.filename))

    def test_read_json(self):
        data = self.obj._read()
        # Reading an empty file
        self.assertIsNone(data)

    def test_read_json_no_existing_file(self):
        self.new_obj = JSONHandler(filename="no.json")
        data = self.obj._read()
        # Reading an not existing file,
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

        # creating the file
        self.obj._create(data=dummy_data)

        # Reading data
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
