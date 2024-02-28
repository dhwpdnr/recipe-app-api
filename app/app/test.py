"""
Sample test
"""

from django.test import SimpleTestCase
from . import calc


class CalcTests(SimpleTestCase):
    """test calc module"""

    def test_add_numbers(self):
        """Test add two numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
