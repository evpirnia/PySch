#!/usr/bin/python3

import sys
from datetime import datetime
import math
from src.appt import Appt

class Scheduler():
    def __init__(self, opening, closing):
        self.opening = opening
        self.closing = closing
        self.appts = []
        self.appt_options = {}
        self.next_opening = self.get_start(datetime.now())
        self.appts_info = [
            "Date",
            "Start",
            "End",
            "Notes"
        ]
        self.menu_options = [
            "List",
            "Schedule",
            "Add",
            "Exit"
        ]
    def get_start(self, now):
        if(now.hour < self.opening):
            now = now.replace(hour=10, minute=0, second=0)
        elif(now.hour >= self.closing):
            now = now.replace(day=now.day+1, hour=10, minute=0, second=0)
        mins = (math.ceil(now.time().minute/15)) * 15
        if mins >= 60:
            mins = mins-60
            hour = (self.opening + 1) % 24
            now = now.replace(hour=hour, minute=mins)
        else:
            now = now.replace(minute=mins)
        return now
    def prompt(self):
        print("====================================================")
        print("Menu:")
        for m in self.menu_options:
            print("* " + m)
        print("====================================================")
        cmd = input("What would you like to do today?\n> ").lower().split()
        cmd = list(filter(lambda x: x != '', cmd))
        if cmd[0] == "list":
            self.display()
        elif cmd[0] == "schedule":
            self.add_appt(cmd[1:])
        elif cmd[0] == "exit":
            print("Goodbye!")
            sys.exit()
        elif cmd[0] == "add":
            # add [schedule_option] for [duration]
            self.add_appt_type(cmd[1], int(cmd[3]))
        else:
            print("Invalid command. Try Again.")
        return
    def add_appt_type(self, schedule_option, duration):
        self.appt_options[schedule_option] = duration
    def add_appt(self, cmd):
        if len(cmd) == 0:
            print("Try Again")
        elif not cmd[0] in self.appt_options:
            print("Not a valid appointment type: %s" % cmd[0])
        else:
            duration = self.appt_options[cmd[0]]
            notes = ' '.join(cmd)
            new_appt = Appt(self.next_opening, duration, notes)
            self.appts.append(new_appt)
            self.next_opening = self.get_start(new_appt.end)
    def display(self):
        if not self.appts:
            print("Your schedule is all clear!")
        else:
            for a in self.appts_info:
                print(a + "\t\t", end="")
            print()
            for a in self.appts:
                a.display()
