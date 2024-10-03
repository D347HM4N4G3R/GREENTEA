import unittest
import easyjson.json_util as ej
import os
import json

class TestEasyJSON(unittest.TestCase):

    def setUp(self):
        self.test_file = "test.json"
        self.test_data = {"name": "EasyJSON", "version": 1.0}

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_json(self):
        ej.save_json(self.test_file, self.test_data)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_json(self):
        ej.save_json(self.test_file, self.test_data)
        loaded_data = ej.load_json(self.test_file)
        self.assertEqual(self.test_data, loaded_data)

if __name__ == "__main__":
    unittest.main()
