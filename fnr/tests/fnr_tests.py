import unittest
from fnr import fnr_core as fnr

class FnrTests(unittest.TestCase):
    print('FnrTests')
    def test_find_and_replace_simple_string(self):
        template = 'Hello, {name}!'
        context = {'name': 'Collin'}
        expected = 'Hello, Collin!'

        actual = fnr.find_and_replace(context, template)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()