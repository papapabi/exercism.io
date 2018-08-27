class Clock(object):
    """A class that handles military time."""

    def __init__(self, hours, minutes):
        self.minutes = minutes % 60
        self.hours = (hours + (minutes // 60)) % 24

    def __repr__(self):
        return '{classname}(hours={hours}, minutes={minutes})'.format(
            classname=self.__class__.__name__,
            hours=self.hours,
            minutes=self.minutes)

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hours, self.minutes) 

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)
