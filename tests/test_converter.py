import unittest

from convert_contacts import remove_others


class TestScript(unittest.TestCase):

    def test_remove_others_normal_input(self):
        test_list = ['2012-02-22 - McQueen, Lightning.pdf']
        self.assertEqual(remove_others(2010, 2020, test_list), ['2012-02-22 - McQueen, Lightning'],
                         'Expected: 2012-02-22 - McQueen, Lightning')

    def test_remove_others_bad_input(self):
        test_list = ['Unknown Date - Builder, Bob the.pdf']
        self.assertEqual(remove_others(2010, 2020, test_list), [],
                         'Expected: empty list')


if __name__ == '__main__':
    unittest.main()