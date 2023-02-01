import unittest
import rectangle_measures


class RectangleTest(unittest.TestCase):
    def test_area(self):
        rectangle = rectangle_measures.Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "Incorrect area")

    def test_perimeter(self):
        rectangle = rectangle_measures.Rectangle(2, 3)
        self.assertEqual(rectangle.get_perimeter(), 10, "Incorrect perimeter")

    def test_dimensions(self):
        rectangle = rectangle_measures.Rectangle(2, 3)
        self.assertEqual(rectangle.retrieve_dimensions(), (2, 3), "Incorrect rectangle")

    def test_diagonal(self):
        rectangle = rectangle_measures.Rectangle(5, 12)
        self.assertEqual(rectangle.get_diagonal(), 13, "Incorrect rectangle")

    def test_negative(self):
        rectangle = rectangle_measures.Rectangle(2, 3)
        self.assertGreaterEqual((rectangle.width and rectangle.height), 0, "Incorrect rectangle, can't be negative")
