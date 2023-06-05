import unittest
from base import Base

class BaseTestCase(unittest.TestCase):
    def test_base_auto_assign_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_auto_assign_id_plus_one(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_base_save_to_file(self):
        b = Base(89)
        Base.save_to_file([b])

        with open("Base.json", "r") as file:
            data = file.read()
            self.assertEqual(data, '[{"id": 89}]')

    def test_base_to_json_string_none(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, '[]')

    def test_base_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, '[]')

    def test_base_to_json_string(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_base_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_base_from_json_string_empty_list(self):
        result = Base.from_json_string('[]')
        self.assertEqual(result, [])

    def test_base_from_json_string(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

if __name__ == '__main__':
    unittest.main()
