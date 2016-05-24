# Create your tests here.
import unittest
from datetime import date
import calendar
from calender import Calender
# import json


class TestCalender(unittest.TestCase):

    def setUp(self):
        self.calender = Calender()

    def tearDown(self):
        self.calender = None

    def today(self):
        the_date = date.today()
        weekday = calendar.day_name[the_date.weekday()]
        str_today = str(the_date)
        numbers = [int(n) for n in str_today.split('-')]
        the_date_for_today = {"month": numbers[1], "day": numbers[2],
                              "year": numbers[0]}
        return the_date_for_today, numbers, weekday

    def test_get_todays_date(self):
        today = self.calender.getToday()
        test_Date, test_Date_Numbers, weekday = self.today()
        self.assertEqual(test_Date, today)

        month = test_Date_Numbers[1]
        self.assertEqual(month, self.calender.month)

        day = test_Date_Numbers[2]
        self.assertEqual(day, self.calender.day)

        year = test_Date_Numbers[0]
        self.assertEqual(year, self.calender.year)

        self.assertEqual(weekday, self.calender.today_WeekDay)

    def test_get_how_many_days_in_month(self):
        days = self.calender.daysThisMonth(11, 2015)
        self.assertEqual(30, days)

        days = self.calender.daysThisMonth(12, 2015)
        self.assertEqual(31, days)

        days = self.calender.daysThisMonth(1, 2016)
        self.assertEqual(31, days)

    def test_find_date_of_week_start_and_date_of_week_end(self):
        start, end = self.calender.startAndEndOfMonth(11, 2015)
        self.assertEqual("Sunday", start)
        self.assertEqual("Monday", end)
        start, end = self.calender.startAndEndOfMonth(12, 2015)
        self.assertEqual("Tuesday", start)
        self.assertEqual("Thursday", end)

        start, end = self.calender.startAndEndOfMonth(1, 2016)
        self.assertEqual("Friday", start)
        self.assertEqual("Sunday", end)

    def test_how_many_rows_for_calender(self):
        rows = self.calender.howManyRowsForMonth(11, 2015)
        self.assertEqual(5, rows)
        rows = self.calender.howManyRowsForMonth(12, 2015)
        self.assertEqual(5, rows)
        rows = self.calender.howManyRowsForMonth(1, 2016)
        self.assertEqual(6, rows)
        rows = self.calender.howManyRowsForMonth(2, 2016)
        self.assertEqual(5, rows)
        rows = self.calender.howManyRowsForMonth(3, 2016)
        self.assertEqual(5, rows)

    def test_structure_of_month(self):
        calendar.setfirstweekday(6)
        expectedAnswer = calendar.monthcalendar(2015, 11)
        monthCalender = self.calender.showMonth(2015, 11)
        self.assertEqual(expectedAnswer, monthCalender)

        expectedAnswer = calendar.monthcalendar(2015, 12)
        monthCalender = self.calender.showMonth(2015, 12)
        self.assertEqual(expectedAnswer, monthCalender)

        expectedAnswer = calendar.monthcalendar(2016, 1)
        monthCalender = self.calender.showMonth(2016, 1)
        self.assertEqual(expectedAnswer, monthCalender)

        # print monthCalender
        # print self.calender.monthlyCalender(1, 2016)

    def test_show_month_calender(self):
        emptyCal = self.calender.buildMonthlyCalender(1, 2016)
        expectedAnswer = {
            1: {'Sunday': {'date': 0}, 'Monday': {'date': 0},
                'Tuesday': {'date': 0}, 'Wednesday': {'date': 0},
                'Thursday': {'date': 0}, 'Friday': {'date': 1},
                'Saturday': {'date': 2}},
            2: {'Sunday': {'date': 3}, 'Monday': {'date': 4},
                'Tuesday': {'date': 5}, 'Wednesday': {'date': 6},
                'Thursday': {'date': 7}, 'Friday': {'date': 8},
                'Saturday': {'date': 9}},
            3: {'Sunday': {'date': 10}, 'Monday': {'date': 11},
                'Tuesday': {'date': 12}, 'Wednesday': {'date': 13},
                'Thursday': {'date': 14}, 'Friday': {'date': 15},
                'Saturday': {'date': 16}},
            4: {'Sunday': {'date': 17}, 'Monday': {'date': 18},
                'Tuesday': {'date': 19}, 'Wednesday': {'date': 20},
                'Thursday': {'date': 21}, 'Friday': {'date': 22},
                'Saturday': {'date': 23}},
            5: {'Sunday': {'date': 24}, 'Monday': {'date': 25},
                'Tuesday': {'date': 26}, 'Wednesday': {'date': 27},
                'Thursday': {'date': 28}, 'Friday': {'date': 29},
                'Saturday': {'date': 30}},
            6: {'Sunday': {'date': 31}, 'Monday': {'date': 0},
                'Tuesday': {'date': 0}, 'Wednesday': {'date': 0},
                'Thursday': {'date': 0}, 'Friday': {'date': 0},
                'Saturday': {'date': 0}}
        }
        self.assertEqual(expectedAnswer, emptyCal)

        emptyCal = self.calender.buildMonthlyCalender(11, 2015)
        expectedAnswer = {
            1: {'Sunday': {'date': 1}, 'Monday': {'date': 2},
                'Tuesday': {'date': 3}, 'Wednesday': {'date': 4},
                'Thursday': {'date': 5}, 'Friday': {'date': 6},
                'Saturday': {'date': 7}},
            2: {'Sunday': {'date': 8}, 'Monday': {'date': 9},
                'Tuesday': {'date': 10}, 'Wednesday': {'date': 11},
                'Thursday': {'date': 12}, 'Friday': {'date': 13},
                'Saturday': {'date': 14}},
            3: {'Sunday': {'date': 15}, 'Monday': {'date': 16},
                'Tuesday': {'date': 17}, 'Wednesday': {'date': 18},
                'Thursday': {'date': 19}, 'Friday': {'date': 20},
                'Saturday': {'date': 21}},
            4: {'Sunday': {'date': 22}, 'Monday': {'date': 23},
                'Tuesday': {'date': 24}, 'Wednesday': {'date': 25},
                'Thursday': {'date': 26}, 'Friday': {'date': 27},
                'Saturday': {'date': 28}},
            5: {'Sunday': {'date': 29}, 'Monday': {'date': 30},
                'Tuesday': {'date': 0}, 'Wednesday': {'date': 0},
                'Thursday': {'date': 0}, 'Friday': {'date': 0},
                'Saturday': {'date': 0}}
        }
        self.assertEqual(expectedAnswer, emptyCal)

        emptyCal = self.calender.buildMonthlyCalender(14, 2015)
        self.assertEqual(None, emptyCal)
        emptyCal = self.calender.buildMonthlyCalender(0, 2015)
        self.assertEqual(None, emptyCal)

    def test_add_event_to_date(self):
        createdEvent = {'event': "Thanks Giving",
                        'info': "", 'location': [],
                        'start': 0, 'end': 24}
        self.calender.addEventToCalender(11, 27, 2015, createdEvent)
        events = self.calender.eventsForDay(11, 27, 2015)
        expectedAnswer = {'events':
                          {1: {'event': "Thanks Giving", 'date': '11-27-2015',
                           'info': "", "location": [], "start": 0, "end": 24}}}
        self.assertEqual(expectedAnswer, events)

        createdEvent = {'event': "Thanks Giving Service",
                        'info': "", 'location': [],
                        'start': 12, 'end': 14}
        self.calender.addEventToCalender(11, 27, 2015, createdEvent)
        events = self.calender.eventsForDay(11, 27, 2015)
        expectedAnswer = {'events':
                          {1: {'event': "Thanks Giving", 'date': '11-27-2015',
                           'info': "", "location": [], "start": 0, "end": 24},
                           2: {'event': "Thanks Giving Service",
                           'date': '11-27-2015', 'info': "",
                               'location': [], 'start': 12, 'end': 14}}}
        self.assertEqual(expectedAnswer, events)
        events = self.calender.eventsForDay(11, 28, 2015)
        self.assertEqual(None, events)

    def test_show_Monthly_Calender(self):
        createdEvent = {'event': "Sunday Service", 'info': "", 'location': [],
                        'start': "11:30am", 'end': "1:00pm"}
        self.calender.addEventToCalender(11, 29, 2015, createdEvent)
        expectedAnswer = {1:
                          {'Monday': {'date': 2},
                           'Tuesday': {'date': 3},
                           'Friday': {'date': 6},
                           'Wednesday': {'date': 4},
                           'Thursday': {'date': 5},
                           'Sunday': {'date': 1},
                           'Saturday': {'date': 7}},
                          2:
                          {'Monday': {'date': 9},
                           'Tuesday': {'date': 10},
                           'Friday': {'date': 13},
                           'Wednesday': {'date': 11},
                           'Thursday': {'date': 12},
                           'Sunday': {'date': 8},
                           'Saturday': {'date': 14}},
                          3:
                          {'Monday': {'date': 16},
                           'Tuesday': {'date': 17},
                           'Friday': {'date': 20},
                           'Wednesday': {'date': 18},
                           'Thursday': {'date': 19},
                           'Sunday': {'date': 15},
                           'Saturday': {'date': 21}},
                          4:
                          {'Monday': {'date': 23},
                           'Tuesday': {'date': 24},
                           'Friday': {'date': 27},
                           'Wednesday': {'date': 25},
                           'Thursday': {'date': 26},
                           'Sunday': {'date': 22},
                           'Saturday': {'date': 28}},
                          5:
                          {'Monday': {'date': 30},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 0},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 29,
                                      1: {'event': "Sunday Service",
                                          'date': '11-29-2015',
                                          'info': "", "location": [],
                                          "start": "11:30am",
                                          "end": "1:00pm"}},
                           'Saturday': {'date': 0}}}

        monthly = self.calender.showMonthCalender(11, 2015)
        self.assertEqual(expectedAnswer[5]["Sunday"][1],
                         monthly[5]["Sunday"][1])
        self.assertEqual(expectedAnswer, monthly)
        monthly = self.calender.showMonthCalender(1, 2016)
        expectedAnswer = {1:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 1},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 0},
                           'Saturday': {'date': 2}},
                          2:
                          {'Monday': {'date': 4},
                           'Tuesday': {'date': 5},
                           'Friday': {'date': 8},
                           'Wednesday': {'date': 6},
                           'Thursday': {'date': 7},
                           'Sunday': {'date': 3},
                           'Saturday': {'date': 9}},
                          3:
                          {'Monday': {'date': 11},
                           'Tuesday': {'date': 12},
                           'Friday': {'date': 15},
                           'Wednesday': {'date': 13},
                           'Thursday': {'date': 14},
                           'Sunday': {'date': 10},
                           'Saturday': {'date': 16}},
                          4:
                          {'Monday': {'date': 18},
                           'Tuesday': {'date': 19},
                           'Friday': {'date': 22},
                           'Wednesday': {'date': 20},
                           'Thursday': {'date': 21},
                           'Sunday': {'date': 17},
                           'Saturday': {'date': 23}},
                          5:
                          {'Monday': {'date': 25},
                           'Tuesday': {'date': 26},
                           'Friday': {'date': 29},
                           'Wednesday': {'date': 27},
                           'Thursday': {'date': 28},
                           'Sunday': {'date': 24},
                           'Saturday': {'date': 30}},
                          6:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 0},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 31},
                           'Saturday': {'date': 0}}}
        self.assertEqual(expectedAnswer, monthly)

        createdEvent = {'event': "Sunday Service", 'info': "", 'location': [],
                        'start': "11:30am", 'end': "1:00pm"}
        self.calender.addEventToCalender(1, 3, 2016, createdEvent)
        createdEvent = {'event': "New Years", 'info': "", 'location': [],
                        'start': "11:30am", 'end': "1:00pm"}
        self.calender.addEventToCalender(1, 1, 2016, createdEvent)
        expectedAnswer = {1:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 1,
                                      1:
                                      {'event': "New Years",
                                       'date': '1-1-2016',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 0},
                           'Saturday': {'date': 2}},
                          2:
                          {'Monday': {'date': 4},
                           'Tuesday': {'date': 5},
                           'Friday': {'date': 8},
                           'Wednesday': {'date': 6},
                           'Thursday': {'date': 7},
                           'Sunday': {'date': 3,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '1-3-2016',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 9}},
                          3:
                          {'Monday': {'date': 11},
                           'Tuesday': {'date': 12},
                           'Friday': {'date': 15},
                           'Wednesday': {'date': 13},
                           'Thursday': {'date': 14},
                           'Sunday': {'date': 10},
                           'Saturday': {'date': 16}},
                          4:
                          {'Monday': {'date': 18},
                           'Tuesday': {'date': 19},
                           'Friday': {'date': 22},
                           'Wednesday': {'date': 20},
                           'Thursday': {'date': 21},
                           'Sunday': {'date': 17},
                           'Saturday': {'date': 23}},
                          5:
                          {'Monday': {'date': 25},
                           'Tuesday': {'date': 26},
                           'Friday': {'date': 29},
                           'Wednesday': {'date': 27},
                           'Thursday': {'date': 28},
                           'Sunday': {'date': 24},
                           'Saturday': {'date': 30}},
                          6:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 0},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 31},
                           'Saturday': {'date': 0}}}
        monthly = self.calender.showMonthCalender(1, 2016)
        # print(json.dumps(monthly, indent=4))
        # print "_______________________________"
        # print "_______________________________"
        # print(json.dumps(expectedAnswer, indent=4))
        self.assertEqual(expectedAnswer, monthly)
        createdEvent = {'event': "New Years Service",
                        'info': "", 'location': [], 'start': "11:30am",
                        'end': "1:00pm"}
        self.calender.addEventToCalender(1, 1, 2016, createdEvent)
        expectedAnswer = {1:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 1,
                                      1:
                                      {'event': "New Years",
                                       'date': '1-1-2016',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"},
                                      2:
                                      {'event': "New Years Service",
                                       'date': '1-1-2016',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 0},
                           'Saturday': {'date': 2}},
                          2:
                          {'Monday': {'date': 4},
                           'Tuesday': {'date': 5},
                           'Friday': {'date': 8},
                           'Wednesday': {'date': 6},
                           'Thursday': {'date': 7},
                           'Sunday': {'date': 3,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '1-3-2016',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 9}},
                          3:
                          {'Monday': {'date': 11},
                           'Tuesday': {'date': 12},
                           'Friday': {'date': 15},
                           'Wednesday': {'date': 13},
                           'Thursday': {'date': 14},
                           'Sunday': {'date': 10},
                           'Saturday': {'date': 16}},
                          4:
                          {'Monday': {'date': 18},
                           'Tuesday': {'date': 19},
                           'Friday': {'date': 22},
                           'Wednesday': {'date': 20},
                           'Thursday': {'date': 21},
                           'Sunday': {'date': 17},
                           'Saturday': {'date': 23}},
                          5:
                          {'Monday': {'date': 25},
                           'Tuesday': {'date': 26},
                           'Friday': {'date': 29},
                           'Wednesday': {'date': 27},
                           'Thursday': {'date': 28},
                           'Sunday': {'date': 24},
                           'Saturday': {'date': 30}},
                          6:
                          {'Monday': {'date': 0},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 0},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 31},
                           'Saturday': {'date': 0}}}
        monthly = self.calender.showMonthCalender(1, 2016)
        self.assertEqual(expectedAnswer, monthly)

    def test_add_recuring_events(self):
        createdEvent = {'event': "Sunday Service", 'info': "",
                        'location': [], 'start': "11:30am", 'end': "1:00pm"}
        self.calender.addReccuringEventToCalender(
            'Sunday', 'weekly', createdEvent)
        answer = self.calender.reccuringEventsForMonth(11, 2015)
        one = {'info': '', 'end': '1:00pm', 'start': '11:30am',
               'location': [], 'date': '11-1-2015', 'event': 'Sunday Service'}
        two = {'info': '', 'end': '1:00pm', 'start': '11:30am',
               'location': [], 'date': '11-8-2015', 'event': 'Sunday Service'}
        three = {'info': '', 'end': '1:00pm', 'start': '11:30am',
                 'location': [], 'date': '11-15-2015',
                 'event': 'Sunday Service'}
        four = {'info': '', 'end': '1:00pm', 'start': '11:30am',
                'location': [], 'date': '11-22-2015',
                'event': 'Sunday Service'}
        five = {'info': '', 'end': '1:00pm', 'start': '11:30am',
                'location': [], 'date': '11-29-2015',
                'event': 'Sunday Service'}
        expected = [one, two, three, four, five]
        # print "what I got"
        # print "{}".format(answer)
        # print "_______________________________"
        # print "_______________________________"
        # print "this is what was expected"
        # print "{}".format(expected)
        self.assertEqual(expected, answer)

    def test_add_recuring_events_to_monthly_calender(self):
        createdEvent = {'event': "Sunday Service", 'info': "",
                        'location': [], 'start': "11:30am", 'end': "1:00pm"}
        expectedAnswer = {1:
                          {'Monday': {'date': 2},
                           'Tuesday': {'date': 3},
                           'Friday': {'date': 6},
                           'Wednesday': {'date': 4},
                           'Thursday': {'date': 5},
                           'Sunday': {'date': 1,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '11-1-2015',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 7}},
                          2:
                          {'Monday': {'date': 9},
                           'Tuesday': {'date': 10},
                           'Friday': {'date': 13},
                           'Wednesday': {'date': 11},
                           'Thursday': {'date': 12},
                           'Sunday': {'date': 8,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '11-8-2015',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 14}},
                          3:
                          {'Monday': {'date': 16},
                           'Tuesday': {'date': 17},
                           'Friday': {'date': 20},
                           'Wednesday': {'date': 18},
                           'Thursday': {'date': 19},
                           'Sunday': {'date': 15,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '11-15-2015',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 21}},
                          4:
                          {'Monday': {'date': 23},
                           'Tuesday': {'date': 24},
                           'Friday': {'date': 27},
                           'Wednesday': {'date': 25},
                           'Thursday': {'date': 26},
                           'Sunday': {'date': 22,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '11-22-2015',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 28}},
                          5:
                          {'Monday': {'date': 30},
                           'Tuesday': {'date': 0},
                           'Friday': {'date': 0},
                           'Wednesday': {'date': 0},
                           'Thursday': {'date': 0},
                           'Sunday': {'date': 29,
                                      1:
                                      {'event': "Sunday Service",
                                       'date': '11-29-2015',
                                       'info': "", "location": [],
                                       "start": "11:30am",
                                       "end": "1:00pm"}},
                           'Saturday': {'date': 0}}}
        self.calender.addReccuringEventToCalender(
            'Sunday', 'weekly', createdEvent)
        monthly = self.calender.showMonthCalender(11, 2015)

        # print "this is what was shown"
        # print(json.dumps(monthly, indent=4))
        # print "_______________________________"
        # print "_______________________________"
        # print "this is what was expected"
        # print(json.dumps(expectedAnswer, indent=4))
        self.assertEqual(expectedAnswer, monthly)

if __name__ == '__main__':
    unittest.main()
