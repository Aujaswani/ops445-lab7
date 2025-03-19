#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day."""
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __add__(self, other):
        sum_hour = self.hour + other.hour
        sum_minute = self.minute + other.minute
        sum_second = self.second + other.second

        while sum_second >= 60:
            sum_second -= 60
            sum_minute += 1

        while sum_minute >= 60:
            sum_minute -= 60
            sum_hour += 1

        sum_hour = sum_hour % 24
        return Time(sum_hour, sum_minute, sum_second)

def valid_time(t):
    if t.hour < 0 or t.hour >= 24:
        return False
    if t.minute < 0 or t.minute >= 60:
        return False
    if t.second < 0 or t.second >= 60:
        return False
    return True

def time_to_sec(t):
    """Convert a Time object into total seconds"""
    return t.hour * 3600 + t.minute * 60 + t.second

def sec_to_time(seconds):
    """Convert total seconds into a Time object"""
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    second = seconds % 60
    return Time(hour, minute, second)

def format_time(t):
    """Return a formatted time string from a Time object"""
    return f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}"
