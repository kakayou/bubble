from django.test import TestCase
from datas.views import latest_term


class DataTestCase(TestCase):

    def setUp(self):
        pass

    def test_max_term(self):
        max_term = latest_term()
        print(max_term)
        self.assertIsNotNone(max_term)