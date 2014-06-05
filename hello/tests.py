from django.test import TestCase

class HelloTestCase(TestCase):

	def test_ok(self):
		self.assertEqual(1, 1)

	def test_not_ok(self):
		self.assertTrue(False)
