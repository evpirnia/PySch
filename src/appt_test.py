#!/usr/bin/python3

import pytest
from appt import Appt
from datetime import datetime

def test_init_appt():
    time_snapshot = datetime.now()
    new_appt = Appt(time_snapshot, 120, "brunch")
    assert new_appt.notes == "brunch"
    assert new_appt.length == 120
    assert new_appt.start == time_snapshot
    assert new_appt.end.hour == new_appt.start.hour + 2

# Handle 11pm appointment cases
def test_handle_1115_pm():
    time_snapshot = datetime.now().replace(hour=23, minute=15)
    new_appt = Appt(time_snapshot, 60, "meeting with tor")
    assert new_appt.end.hour == 0
    assert new_appt.end.minute == 15


def test_handle_1130_pm():
    time_snapshot = datetime.now().replace(hour=23, minute=30)
    new_appt = Appt(time_snapshot, 30, "ice cream with friends")
    assert new_appt.end.hour == 0
    assert new_appt.end.minute == 0
