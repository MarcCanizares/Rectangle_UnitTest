import unittest
import rectangle_measures
import rectangle_test

if __name__ == '__main__':
    rectangle = rectangle_measures.Rectangle(20, 10)
    print(f"The dimensions of the rectangle are:\t {rectangle.retrieve_dimensions()}")
    rectangle.set_width(200)
    rectangle.set_height(100)
    print(f"The dimensions of the rectangle are: {rectangle.retrieve_dimensions()}")
    print(f"These are the tests of the code")
    print(f"The diagonal of the rectangle is: {rectangle.get_diagonal()}")
    rectangle_test_class = unittest.TestLoader().loadTestsFromModule(rectangle_test)
    unittest.TextTestRunner(verbosity=2).run(rectangle_test_class)
