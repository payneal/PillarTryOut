from datetime import date
import calendar

# needed to psss test - test_show_Monthly_Calender
calendar.setfirstweekday(6)

import numpy as np
from copy import deepcopy


class Calender(object):

    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        self.today_WeekDay = None
        self.events = []
        self.reccuringEvents = []
        self.setToday()

    def setToday(self):
        the_date = date.today()
        today = str(the_date)  # ex. '1-1-2015' => numbers=[1,1,2015]
        numbers = [int(n) for n in today.split('-')]
        self.setCurrentYearMonthDay(numbers)
        self.today_WeekDay = calendar.day_name[the_date.weekday()]

    def setCurrentYearMonthDay(self, numbers):
        self.year = numbers[0]
        self.month = numbers[1]
        self.day = numbers[2]

    def getToday(self):
        the_date_for_today = {
            "month": self.month,
            "day": self.day,
            "year": self.year
        }
        return the_date_for_today

    def daysThisMonth(self, month, year):
        if month == 12:
            return (date(year+1, 1, 1) - date(year, month, 1)).days
        else:
            return (date(year, month+1, 1) - date(year, month, 1)).days

    def convertDayToWeekDayName(self, day, month, year):
        the_date = date(year, month, day)
        return calendar.day_name[the_date.weekday()]

    def startAndEndOfMonth(self, month, year):
        start = self.convertDayToWeekDayName(1, month, year)
        lastDay = self.daysThisMonth(month, year)
        end = self.convertDayToWeekDayName(lastDay, month, year)
        return start, end

    def howManyRowsForMonth(self, month, year):
        start_date_name, end_date_name = self.startAndEndOfMonth(month, year)
        days = self.daysThisMonth(month, year)
        amount = days / 7

        if end_date_name == "Sunday":
            return amount + 2
        return amount + 1

    def showMonth(self, year, month):
        calendar.setfirstweekday(6)
        return calendar.monthcalendar(year, month)

    def dayNameToNumber(self, dayName):
        days = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4,
                "Thursday": 5, "Friday": 6, "Saturday": 7
                }

        return days[dayName]

    def getNumOfWeeks_startWeekday_endWeekday_TotaldaysOf(self, month, year):
        number_of_weeks = self.howManyRowsForMonth(month, year)
        start, end = self.startAndEndOfMonth(month, year)
        total_Days = self.daysThisMonth(month, year)
        return number_of_weeks, start, end, total_Days

    def setUpWeek(self):
        week_Json = {"Sunday": {}, "Monday": {},
                     "Tuesday": {},
                     "Wednesday": {}, "Thursday": {}, "Friday": {},
                     "Saturday": {}
                     }
        week_list = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday",
                     "Friday", "Saturday"
                     ]
        weekNumber = 1
        count = 1
        return week_Json, week_list, weekNumber, count

    def buildMonthlyCalender(self, month, year):
        if month > 12 or month < 1:
            return None

        number_of_weeks, start, end, total_Days = \
            self.getNumOfWeeks_startWeekday_endWeekday_TotaldaysOf(month, year)
        week_Json, week_list, weekNumber, count = self.setUpWeek()

        neededInfo = [number_of_weeks, weekNumber,
                      week_list, start, count, total_Days]
        return self.buildingTheDictionayOfMonthlyCal(neededInfo)

    def buildingTheDictionayOfMonthlyCal(self, neededInfo):
        number_of_weeks = neededInfo[0]
        weekNumber = neededInfo[1]
        week_list = neededInfo[2]
        start = neededInfo[3]
        count = neededInfo[4]
        total_Days = neededInfo[5]

        monthlyCalender = {}
        for x in range(number_of_weeks):
            monthlyCalender[weekNumber] = {}
            for day in week_list:
                if weekNumber == 1:
                    if self.dayNameToNumber(day) >= \
                            self.dayNameToNumber(start):
                        monthlyCalender[weekNumber][day] = {'date': count}
                        count = count + 1
                    else:
                        monthlyCalender[weekNumber][day] = {'date': 0}
                else:
                    if count > total_Days:
                        monthlyCalender[weekNumber][day] = {'date': 0}
                    else:
                        monthlyCalender[weekNumber][day] = {'date': count}
                        count += 1
            weekNumber += 1
        return monthlyCalender

    def addEventToCalender(self, month, day, year, event):
        stringDate = "{}-{}-{}".format(month, day, year)
        event['date'] = stringDate
        self.events.append(event)

    def eventsForDay(self, month, day, year):
        stringDate = "{}-{}-{}".format(month, day, year)

        allEvents = {'events': {}}
        COUNT = 1
        for item in self.events:
            if item['date'] == stringDate:
                eventNumber = COUNT
                allEvents['events'][eventNumber] = item
                COUNT = COUNT + 1

        if allEvents == {'events': {}}:
            return None
        else:
            return allEvents

    def get_week_of_month(self, year, month, day):
        x = np.array(calendar.monthcalendar(year, month))
        week_of_month = np.where(x == day)[0][0] + 1
        return week_of_month

    def addReccuringEventToCalender(self, dayOfWeek, howOften, eventToAdd):
        eventToAdd['dayOfweek'] = dayOfWeek
        eventToAdd['occurrence'] = howOften
        self.reccuringEvents.append(eventToAdd)

    def reccuringEventsForMonth(self, month, year, monthlyCall=None):
        self.month = month
        self.year = year
        days = calendar.monthrange(year, month)
        if monthlyCall is None:
            hold = []

        for event in self.reccuringEvents:
            dayOfweek = event['dayOfweek']
            howManyTimesDayOfWeekIsInMonth, theDaysThatMatch = \
                self.numberOfTimesDayisInMOnth(days, dayOfweek)

            for weekNumber in range(howManyTimesDayOfWeekIsInMonth):
                exactdate = theDaysThatMatch[weekNumber]
                eventCopy = deepcopy(event)
                del eventCopy['occurrence']
                del eventCopy['dayOfweek']

                eventCopy['date'] = '{}-{}-{}'.format(month, exactdate, year)
                if monthlyCall:
                    monthlyCall[weekNumber+1][dayOfweek][1] = eventCopy
                else:
                    hold.append(eventCopy)
        if monthlyCall is None:
            return hold
        else:
            return monthlyCall

    def showMonthCalender(self, month, year):
        monthlyCal = self.buildMonthlyCalender(month, year)
        for event in self.events:
            date = event['date']
            numbers = [int(n) for n in date.split('-')]
            event_date = {"day": numbers[1], "month": numbers[0],
                          "year": numbers[2]
                          }
            NameOfTheWeekDay = \
                self.convertDayToWeekDayName(event_date['day'],
                                             event_date['month'],
                                             event_date['year'])
            weekNumberInMonth = self.get_week_of_month(event_date['year'],
                                                       event_date['month'],
                                                       event_date['day']
                                                       )
            infoNeeded = [month, year, event_date, monthlyCal,
                          NameOfTheWeekDay, weekNumberInMonth, event]
            monthlyCal = self.grabNonRecurringEvent(infoNeeded)

        if len(self.reccuringEvents) > 0:
            monthlyCal = self.addRecurringEvents(month, year, monthlyCal)

        return monthlyCal

    def grabNonRecurringEvent(self, infoNeeded):
        month = infoNeeded[0]
        year = infoNeeded[1]
        event_date = infoNeeded[2]
        monthlyCal = infoNeeded[3]
        NameOfTheWeekDay = infoNeeded[4]
        weekNumberInMonth = infoNeeded[5]
        event = infoNeeded[6]
        if event_date['month'] == month and event_date['year'] == year:
                # we Know we are on the same month and same year

            # check if event 1 exist
            if 1 in monthlyCal[weekNumberInMonth][NameOfTheWeekDay]:
                # if it does find how many events that have been created
                count = 0
                for idx in \
                        monthlyCal[weekNumberInMonth][NameOfTheWeekDay]:
                    count += 1
                monthlyCal[weekNumberInMonth][NameOfTheWeekDay][count] = event
            else:
                # if it doent then we need to create it
                monthlyCal[weekNumberInMonth][NameOfTheWeekDay][1] = event
        return monthlyCal

    def numberOfTimesDayisInMOnth(self, days, dayOfweek):
        howManyTimesDayOfWeekIsInMonth = 0

        theDaysThatMatch = []
        for number in range(days[1]):
            dayNumber = (calendar.weekday(
                         self.year, self.month, number+1)+1) % 7
            week = [
                'Sunday', "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"
            ]

            if week[dayNumber] == dayOfweek:
                theDaysThatMatch.append(number+1)
                howManyTimesDayOfWeekIsInMonth += 1

        return howManyTimesDayOfWeekIsInMonth, theDaysThatMatch

    def addRecurringEvents(self,  month, year, monthlyCal):
        return self.reccuringEventsForMonth(month, year, monthlyCal)
