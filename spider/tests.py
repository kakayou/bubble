from django.test import TestCase
from spider.crawler import get_last_term


class SpiderTestCase(TestCase):

    def setUp(self):
        pass

    def test_max_term(self):
        max_term = get_last_term()
        print(max_term)
        self.assertIsNotNone(max_term)
