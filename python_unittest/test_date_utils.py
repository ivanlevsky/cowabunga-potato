import unittest
from python_common.date_time_utils import DateUtils



class TestStringUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old_date = '2021-08-25*'
        cls.calc_date1 = 10
        cls.calc_date2 = -10
        cls.first_day_of_month = '2020-02-25'
        cls.last_day_of_month = '2021-08-01'

    def test_split_string_by_regex(self):
        with self.subTest():
            self.assertEqual('2021-09-04', DateUtils.calcu(self.bin_decoded_text))

if __name__ == '__main__':
    unittest.main()