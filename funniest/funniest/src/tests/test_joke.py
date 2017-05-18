from unittest import TestCase

import main


class TestJoke(TestCase):
    def test_is_string(self):
        s = main.joke()
        self.assertTrue(isinstance(s, basestring))
