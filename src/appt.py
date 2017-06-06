#!/usr/bin/python3
import math

class Appt():
    def __init__(self, start, length, notes):
        self.start = start
        self.length = length
        self.notes = notes
        self.end = self.get_end()
    def display(self):
        print("%s\t%s\t%s\t%s"
                % (self.start.date().strftime("%x"),
                self.start.time().strftime("%I:%M %p"),
                self.end.time().strftime("%I:%M %p"),
                self.notes))
    def get_end(self):
        numhours = math.floor((self.start.minute + self.length) / 60)
        hour = (self.start.hour + numhours) % 24
        mins = (self.start.minute + self.length) % 60
        end = self.start.replace(hour=hour, minute=mins)
        return end
