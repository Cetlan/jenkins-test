import unittest
from jtest import add, sub

class TestOps(unittest.TestCase):
	def test_add(self):
		self.assertEqual(add(1, 2), 3)

	def test_sub(self):
		self.assertEqual(sub(3, 4), 1)
