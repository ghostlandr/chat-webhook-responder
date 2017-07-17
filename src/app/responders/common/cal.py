import calendar

import datetime

from app.responders.slack import SlackCommandResponder


class CalSlackResponder(SlackCommandResponder):

    def process(self, args):
        """
        Return a pretty-printed monthly calendar
        """
        return "```{}```".format(calendar.TextCalendar().formatmonth(*self.determine_date(args)))

    @staticmethod
    def determine_date(args):
        """
        Determine month/year to print, there are 3 possibilities:
        1. User specifies both month and year
        2. User specifies only month, default to current year
        3. User specifies nothing, default to current month and year
        """
        now = datetime.datetime.now()
        date = args["text"].split(" ")
        month = date[0]
        if month and len(date) > 1:
            return int(date[1]), int(month)
        elif month:
            return now.year, int(month)
        else:
            return now.year, now.month


