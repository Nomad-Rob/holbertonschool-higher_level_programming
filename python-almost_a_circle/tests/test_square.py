import unittest
from models.square import Square


class SquareTestCase(unittest.TestCase):
    def test_square_init_with_side(self):
        s = Square(1)
        self.assertEqual(s.id, None)
        self.assertEqual(s.size, 1)

    def test_square_init_with_side_and_position(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.id, None)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_init_with_non_integer_side(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_init_with_non_integer_side_and_position(self):
        with self.assertRaises(TypeError):
            Square(1, "2", 3)

    def test_square_init_with_non_integer_position(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_init_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
            Square(1, 2, 3, 4)

    def test_square_init_with_negative_side(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_init_with_negative_side_and_position(self):
        with self.assertRaises(ValueError):
            Square(1, -2, 3)

    def test_square_init_with_negative_position(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_str_method(self):
        s = Square(1, 2, 3)
        self.assertEqual(str(s), "[Square] (None) 2/3 - 1")

    def test_square_to_dictionary_method(self):
        s = Square(1, 2, 3)
        expected = {'id': None, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected)

    def test_square_update_method(self):
        s = Square(1, 2, 3)
        s.update(89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_method_with_size(self):
        s = Square(1, 2, 3)
        s.update(89, 4)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_method_with_size_and_position(self):
        s = Square(1, 2, 3)
        s.update(89, 4, 5, 6)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_square_update_method_with_kwargs_id(self):
        s = Square(1, 2, 3)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_method_with_kwargs_size(self):
        s = Square(1, 2, 3)
        s.update(**{'id': 89, 'size': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_update_method_with_kwargs_size_and_position(self):
        s = Square(1, 2, 3)
        s.update(**{'id': 89, 'size': 4, 'x': 5, 'y': 6})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_square_create_method_with_kwargs_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_create_method_with_kwargs_size(self):
        s = Square.create(**{'id': 89, 'size': 4})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_create_method_with_kwargs_size_and_position(self):
        s = Square.create(**{'id': 89, 'size': 4, 'x': 5, 'y': 6})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 6)

    def test_square_save_to_file_method_with_none_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file(None)

    def test_square_save_to_file_method_with_empty_list_argument(self):
        with self.assertRaises(ValueError):
            Square.save_to_file([])

    def test_square_save_to_file_method_with_valid_list_argument(self):
        Square.save_to_file([Square(1, 2, 3)])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertNotEqual(content, "")

    def test_square_load_from_file_method_when_file_does_not_exist(self):
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_square_load_from_file_method_when_file_exists(self):
        Square.save_to_file([Square(1, 2, 3)])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].id, 1)
        self.assertEqual(squares[0].size, 2)
        self.assertEqual(squares[0].x, 3)
        self.assertEqual(squares[0].y, 0)


if __name__ == '__main__':
    unittest.main()
