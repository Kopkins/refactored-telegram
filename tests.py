
import unittest
from Datetime import Datetime

class DatetimeTest(unittest.TestCase):
    def test_datetime_members_afternoon(self):
        string = 'Feb 21 2017 10:19:000 PM'
        d = Datetime.from_api_string(string)
        self.assertEqual('Feb', d.month)
        self.assertEqual(21, d.day)
        self.assertEqual(2017, d.year)
        self.assertEqual(22, d.hour)
        self.assertEqual(19, d.minute)

    def test_datetime_members_morning(self):
        string = 'Feb 21 2017 10:19:000 AM'
        d = Datetime.from_api_string(string)
        self.assertEqual('Feb', d.month)
        self.assertEqual(21, d.day)
        self.assertEqual(2017, d.year)
        self.assertEqual(10, d.hour)
        self.assertEqual(19, d.minute)

    def test_datetime_string(self):
        string = 'Feb 21 2017 10:19:000 AM'
        d = Datetime.from_api_string(string)
        self.assertEqual("10:19 AM", str(d))

    def test_zero_minute(self):
        string = 'Feb 21 2017 10:00:000 AM'
        d = Datetime.from_api_string(string)
        self.assertEqual("10:00 AM", str(d))

    def test_minute_less_than_ten(self):
        string = 'Feb 21 2017 10:04:000 AM'
        d = Datetime.from_api_string(string)
        self.assertEqual("10:04 AM", str(d))

    def test_minute_equal_ten(self):
        string = 'Apr 11 2017 3:10:000 PM'
        d = Datetime.from_api_string(string)
        self.assertEqual("3:10 PM", str(d))

    def test_new_api_string(self):
        string = '2017-09-19 16:47:00.000'
        d = Datetime.from_api_string(string)
        self.assertEqual("4:47 PM", str(d))
        

if __name__ == '__main__':
    unittest.main()
