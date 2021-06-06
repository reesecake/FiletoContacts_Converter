import unittest

from convert_contacts import remove_others, get_filename_data


class TestRemoveOthers(unittest.TestCase):

    def test_remove_others_normal_input(self):
        test_list = ['2012-02-22 - McQueen, Lightning.pdf']
        self.assertEqual(remove_others(2010, 2020, test_list), ['2012-02-22 - McQueen, Lightning'],
                         'Expected: 2012-02-22 - McQueen, Lightning')

    def test_remove_others_bad_input(self):
        test_list = ['Unknown Date - Builder, Bob the.pdf']
        self.assertEqual(remove_others(2010, 2020, test_list), [],
                         'Expected: empty list')

    def test_remove_others_out_of_range(self):
        test_list = ['1940-07-27 - Bunny, Bugs.pdf']
        self.assertEqual(remove_others(2010, 2020, test_list), [],
                         'Expected: empty list')


class TestGetFilenameData(unittest.TestCase):

    def test_get_filename_data(self):
        test_name = '2014-03-18 - Lincoln, Abraham'
        expected_return = [{'First Name': 'Abraham', 'Middle Name': '',
                            'Last Name': 'Lincoln', 'Consult Date': '2014-03-18 '}]
        self.assertEqual(get_filename_data(test_name), expected_return)

    def test_get_filename_data_two_names(self):
        test_name = '2014-03-18 - Lincoln, Abraham & Washington, George'
        expected_return = [{'First Name': 'Abraham', 'Middle Name': '',
                            'Last Name': 'Lincoln', 'Consult Date': '2014-03-18 '},
                           {'First Name': 'George', 'Middle Name': '',
                            'Last Name': 'Washington', 'Consult Date': '2014-03-18 '}]
        self.assertEqual(get_filename_data(test_name), expected_return)


if __name__ == '__main__':
    unittest.main()
