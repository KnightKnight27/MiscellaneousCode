"""
Technical Task - Cron Expression Parser

Write a command line application or script which parses a cron string and expands each field
to show the times at which it will run. You may use whichever language you feel most
comfortable with.

You should only consider the standard cron format with five time fields (minute, hour, day of
month, month, and day of week) plus a command, and you do not need to handle the special
time strings such as "@yearly". The input will be on a single line.

The cron string will be passed to your application as a single argument.
~$ your-program ＂*/15 0 1,15 * 1-5 /usr/bin/find＂

The output should be formatted as a table with the field name taking the first 14 columns and
the times as a space-separated list following it.

For example, the following input argument:

*/15 0 1,15 * 1-5 /usr/bin/find

Should yield the following output:

minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find

You should spend no more than three hours on this exercise. If you do not have time to
handle all possible cron strings then an app which handles a subset of them correctly is
better than one which does not run or produces incorrect results. You will be asked to extend
the solution with additional features while onsite.

You should see your project reviewer as a new team member you are handing the project
over to. Provide everything you feel would be relevant for them to ramp up quickly, such as
tests, a README and instructions for how to run your project in a clean OS X/Linux
environment.

*,- and maybe % for commands
"""

import argparse

from dataclasses import dataclass
from typing import List


@dataclass
class CronSchedule:
    minutes: List
    hours: List
    days_of_month: List
    months: List
    days_of_week: List
    command: str


def parse_minutes_field(input: str) -> List[int]:
    if input == "*":
        return list(range(1, 61))
    elif "-" in input:
        start, end = input.split("-")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(input)]


def parse_hours_field(input: str) -> List[int]:
    if input == "*":
        return list(range(1, 25))
    elif "-" in input:
        start, end = input.split("-")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(input)]


def parse_days_of_month_field(input: str) -> List[int]:
    if input == "*":
        return list(range(1, 32))
    elif "-" in input:
        start, end = input.split("-")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(input)]


def parse_months_field(input: str) -> List[int]:
    if input == "*":
        return list(range(1, 13))
    elif "-" in input:
        start, end = input.split("-")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(input)]


def parse_days_of_week_field(input: str) -> List[int]:
    if input == "*":
        return list(range(1, 8))
    elif "-" in input:
        start, end = input.split("-")
        return list(range(int(start), int(end) + 1))
    else:
        return [int(input)]


def parse_command_field(input: str) -> str:
    return input


def parse_cron_string(cron_string: str) -> CronSchedule:
    fields = cron_string.split()

    minutes = parse_minutes_field(
        fields[0]
    )
    hours = parse_hours_field(
        fields[1]
    )
    days_of_month = parse_days_of_month_field(
        fields[2]
    )
    months = parse_months_field(
        fields[3]
    )
    days_of_week = parse_days_of_week_field(
        fields[4]
    )
    command = parse_command_field(
        fields[5]
    )

    return CronSchedule(
        minutes=minutes,
        hours=hours,
        days_of_month=days_of_month,
        months=months,
        days_of_week=days_of_week,
        command=command,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse cron string and print out field values")
    parser.add_argument("cron_string", type=str, help="Input string in cron format")
    args = parser.parse_args()
    parse_cron_string(args.cron_string)
