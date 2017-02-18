import unittest

from create_box import create_box

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

error_expected = 'Invalid dimensions, height and/or width must be at least equal to 1.'


class TestCreateBox(unittest.TestCase):
    def test_empty_box(self):
        self.assertEqual(create_box(5, 5, '$'), third_box_expected)
        
    def test_empty_box_error(self):
        self.assertEqual(create_box(0, 0, '#'), error_expected)

