from app.responders.common.cal import CalSlackResponder
from freezegun import freeze_time
from unittest import TestCase


@freeze_time("2017-07-15")
class CalSlackResponderTest(TestCase):

    def test_determine_date_returns_current_month_year_if_user_specifies_no_args(self):
        result = CalSlackResponder.determine_date({"text": ""})
        self.assertTupleEqual((2017, 7), result)

    def test_determine_date_returns_specified_month_and_current_year_if_user_specifies_month_args(self):
        result = CalSlackResponder.determine_date({"text": "3"})
        self.assertTupleEqual((2017, 3), result)

    def test_determine_date_returns_specified_month_and_year_if_user_specifies_both_month_and_year(self):
        result = CalSlackResponder.determine_date({"text": "09 1988"})
        self.assertTupleEqual((1988, 9), result)

    def test_process_prints_out_calendar(self):
        expected_calendar = '```     July 2017\nMo Tu We Th Fr Sa Su\n                1  2\n 3  4  5  6  7  8  9\n10 11 12 13 14 15 16\n17 18 19 20 21 22 23\n24 25 26 27 28 29 30\n31\n```'
        result = CalSlackResponder().process({"text": ""})
        self.assertEqual(expected_calendar, result)

