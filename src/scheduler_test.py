#!/usr/bin/python3

import pytest
from scheduler import Scheduler
from datetime import datetime

def test_init_scheduler():
    new_scheduler = Scheduler(10, 18)
    time_snapshot = datetime.now().replace(hour=9)
    assert new_scheduler.opening == 10
    assert new_scheduler.closing == 18
    assert len(new_scheduler.appts) == 0
    assert len(new_scheduler.appt_options) == 0

def test_before_opening():
    new_scheduler = Scheduler(10, 18)
    time_snapshot = datetime.now().replace(hour=8)
    new_scheduler.next_opening = new_scheduler.get_start(time_snapshot)
    assert new_scheduler.next_opening.hour == 10
    assert new_scheduler.next_opening.day == time_snapshot.day

def test_after_closing():
    new_scheduler = Scheduler(10, 18)
    time_snapshot = datetime.now().replace(hour=20)
    new_scheduler.next_opening = new_scheduler.get_start(time_snapshot)
    assert new_scheduler.next_opening.hour == 10
    assert new_scheduler.next_opening.day == time_snapshot.day + 1

def test_add_appt_type():
    new_scheduler = Scheduler(10, 18)
    time_snapshot = datetime.now().replace(hour=10, minute=0)
    new_scheduler.add_appt_type("interview", 60)
    assert len(new_scheduler.appt_options) == 1
    assert new_scheduler.appt_options["interview"] == 60

def test_add_appt():
    new_scheduler = Scheduler(10, 18)
    time_snapshot = datetime.now().replace(hour=10, minute=0)
    new_scheduler.next_opening = time_snapshot
    new_scheduler.add_appt_type("interview", 60)
    cmd = ['interview', 'for', 'jane']
    new_scheduler.add_appt(cmd)
    assert new_scheduler.appts.append != 0
    assert new_scheduler.next_opening.hour == 11
