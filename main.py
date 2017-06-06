#!/usr/bin/python3

# main.py
# a command-line program in Python3 that keeps track of the user's appointments

import sys
from sys import argv
from src.scheduler import Scheduler

def main(argv):
    print("Welcome!")
    new_scheduler = Scheduler(int(argv[1]), int(argv[2]))
    while True:
        new_scheduler.prompt()

main(argv)
