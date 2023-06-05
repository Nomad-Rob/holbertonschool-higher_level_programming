import unittest
from rectangle import Rectangle

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_with_width_height(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_with_width_height_x(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_with_width_height_x_y(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_with_string_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_rectangle_with_string_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_rectangle_with_string_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

    def test_rectangle_with_string_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

    def test_rectangle_with_extra_argument(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5)

    def test_rectangle_with_negative_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2)

    def test_rectangle_with_negative_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2)

    def test_rectangle_with_zero_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

    def test_rectangle_with_zero_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_rectangle_with_negative_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_rectangle_with_negative_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_str(self):
        r = Rectangle(3, 4, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 3/4")

    def test_rectangle_display_without_x_y(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        self.assertEqual(r.display(), expected_output)

    def test_rectangle_display_without_y(self):
        r = Rectangle(3, 2, 1)
        expected_output = " ###\n ###\n"
        self.assertEqual(r.display(), expected_output)

    def test_rectangle_display(self):
        r = Rectangle(3, 2, 1, 2)
        expected_output = "\n\n ###\n ###\n"
        self.assertEqual(r.display(), expected_output)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(3, 4, 1, 2)
        expected_dict = {'x': 1, 'y': 2, 'id': 1, 'height': 4, 'width': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_rectangle_update(self):
        r = Rectangle(3, 4)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_with_width(self):
        r = Rectangle(3, 4)
        r.update(89, 1)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_update_with_width_height(self):
        r = Rectangle(3, 4)
        r.update(89, 1, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_update_with_width_height_x(self):
        r = Rectangle(3, 4)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_update_with_width_height_x_y(self):
        r = Rectangle(3, 4)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_update_with_dictionary_id(self):
        r = Rectangle(3, 4)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_update_with_dictionary_width(self):
        r = Rectangle(3, 4)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_update_with_dictionary_width_height(self):
        r = Rectangle(3, 4)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_update_with_dictionary_width_height_x(self):
        r = Rectangle(3, 4)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_update_with_dictionary_width_height_x_y(self):
        r = Rectangle(3, 4)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_create_with_dictionary_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_rectangle_create_with_dictionary_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)

    def test_rectangle_create_with_dictionary_width_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_create_with_dictionary_width_height_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_rectangle_create_with_dictionary_width_height_x_y(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_rectangle_save_to_file_with_none(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(None)

    def test_rectangle_save_to_file_with_empty_list(self):
        with self.assertRaises(ValueError):
            Rectangle.save_to_file([])

    def test_rectangle_save_to_file_with_valid_list(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        Rectangle.save_to_file([r1, r2])

    def test_rectangle_load_from_file_with_nonexistent_file(self):
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_rectangle_load_from_file_with_existing_file(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)

if __name__ == '__main__':
    unittest.main()
