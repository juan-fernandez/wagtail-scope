from django.test import TestCase

class BasicTestCase(TestCase):
    def test_basic(self):
        self.assertEqual(True, True)