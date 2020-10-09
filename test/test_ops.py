import unittest
from jtest import add

class TestOps(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(1, 2), 3)

