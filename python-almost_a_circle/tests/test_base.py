import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    # Setup and teardown methods are called before and after each test

    def setUp(self):
        """Set up the test environment"""
        # Redirect standard output to a StringIO object to capture print statements
        self.capture_output = io.StringIO()
        sys.stdout = self.capture_output

        # Reset the __nb_objects counter and create a Base instance
        Base._Base__nb_objects = 0
        self.base = Base()

    def tearDown(self):
        """Clean up the test environment"""
        # Restore the standard output
        sys.stdout = sys.__stdout__

        # Delete the Base instance and remove the "Base.json" file if it exists
        del self.base
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass

    def test_print(self):
        """Test the print method"""
        # Print "Hello, world!" and assert the captured output matches
        print("Hello, world!")
        self.assertEqual(self.capture_output.getvalue(), "Hello, world!\n")

    def test_id(self):
        """Test the id assignment in the Base class"""
        # Test id assignment for a new Base instance
        self.assertEqual(self.base.id, 1)

        # Create a Base instance with a specific id
        base2 = Base(50)
        self.assertEqual(base2.id, 50)

        # Create another Base instance without an id argument
        base3 = Base()
        self.assertEqual(base3.id, 2)

    def test_too_many_args(self):
        """Test handling too many arguments in the Base constructor"""
        # Test passing too many arguments to the Base constructor
        with self.assertRaises(TypeError):
            Base(1, 1, 1, 1, 1, 1, 1)

    def test_to_json_string(self):
        """Test the to_json_string method"""
        # Test empty list
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test None
        self.assertEqual(Base.to_json_string(None), "[]")

        # Test a normal list of dictionaries
        list_directories = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        ]
        expected_json = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        self.assertEqual(Base.to_json_string(list_directories), expected_json)

    def test_from_json_string(self):
        """Test the from_json_string method"""
        # Test empty string
        self.assertEqual(Base.from_json_string(""), [])

        # Test empty list
        self.assertEqual(Base.from_json_string("[]"), [])

        # Test None
        self.assertEqual(Base.from_json_string(None), [])

        # Test a valid JSON string
        json_string = (
            '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, '
            '{"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]')
        
        expected_list = [
            {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
            {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

        # Test handling of invalid JSON string
        with self.assertRaises(ValueError):
            Base.from_json_string("invalid")

    def test_save_to_file(self):
        """Test the save_to_file method"""
        # Test handling of None by creating an empty file
        Base.save_to_file(None)
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

        # Test handling of an empty list to create an empty file
        Base.save_to_file([])
        with open("Base.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
