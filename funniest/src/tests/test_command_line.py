from unittest import TestCase

from main.command_line import main


class TestCmd(TestCase):
    def test_basic(self):
        main()
