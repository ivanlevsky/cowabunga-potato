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
            self.assertEqual('2021-09-04', DateUtils.calculate_date(self.old_date, self.calc_date1, False))
        with self.subTest():
            self.assertEqual('2021-09-08', DateUtils.calculate_date(self.old_date, self.calc_date1, True))
        with self.subTest():
            self.assertEqual('2021-08-15', DateUtils.calculate_date(self.old_date, self.calc_date2, False))
        with self.subTest():
            self.assertEqual('2021-08-11', DateUtils.calculate_date(self.old_date, self.calc_date2, True))
        with self.subTest():
            self.assertEqual('2020-02-01', DateUtils.get_first_day_of_month(self.first_day_of_month))
        with self.subTest():
            self.assertEqual('2021-08-31', DateUtils.get_last_day_of_month(self.last_day_of_month))
		with self.subTest():
            self.assertEqual(True, DateUtils.is_day_weekends('2021-08-29'))
        with self.subTest():
            self.assertEqual(False, DateUtils.is_day_weekends('2021-08-30'))
			
if __name__ == '__main__':
    unittest.main()