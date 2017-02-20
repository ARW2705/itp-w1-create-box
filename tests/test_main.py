import unittest

from create_box import create_box
from create_box import create_empty_box

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
$$$$$
$   $
$   $
$   $
$$$$$
""".lstrip()

error_expected = 'Invalid dimensions, height and/or width must be at least 1.'


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_box_error(self):
        self.assertEqual(create_box(0, 0, '#'), error_expected)

    def test_empty_box(self):
        self.assertEqual(create_empty_box(5, 5, '$'), third_box_expected)
          
    def test_empty_box_error(self):
        self.assertEqual(create_empty_box(0, 0, '#'), error_expected)
