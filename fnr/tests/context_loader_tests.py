import unittest
import os
from fnr.context_loader import file_loader

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'examples', 'example_context.csv')

class ContextLoaderTests(unittest.TestCase):
    print('Context loader tests')
    def test_file_loader(self):
        expected = {'Promotion':' Dragons', 'Ham':' Cheese', 'Up':' Down'}

        dut = file_loader.file_loader(TESTDATA_FILENAME)
        actual = dut.get_context_vars()

        self.assertDictEqual(expected, actual)
