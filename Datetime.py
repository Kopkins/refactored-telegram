
import re

class Datetime():
    def __init__(self, mon, day, year, hour, minute):
        self.month = mon
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute

    def __str__(self):
        time_of_day = 'PM' if self.hour > 12 else 'AM'
        hour = self.hour if time_of_day == 'AM' else self.hour - 12
        minute = self.minute if self.minute != 0 else '00'
        return '{}:{} {}'.format(hour, minute, time_of_day)

    def from_api_string(string):
        pattern = re.compile("([A-Za-z]{3,}) (\d{,2}) (\d{,4}) (\d{,2}):(\d{,2}):.*([AP]M)\Z")
        match = pattern.match(string)
        mon, day, year, hour, minute, time_of_day = match.group(1, 2, 3, 4, 5, 6)
        day, year, hour, minute = map(int, [day, year, hour, minute])
        if time_of_day == 'PM':
            hour += 12
        return Datetime(mon, day, year, hour, minute)
