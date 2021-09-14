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


def _parse_field(field: str, min_value: int, max_value: int):
    if field == "*":
        return list(range(min_value, max_value + 1))
    elif field.startswith("*/"):
        step = int(field.split("/")[1])
        return list(range(min_value, max_value + 1, step))
    elif "-" in field:
        start, end = field.split("-")
        return list(range(int(start), int(end) + 1))
    elif "," in field:
        return [int(x) for x in field.split(",")]
    else:
        return [int(field)]


def parse_minutes_field(field: str) -> List[int]:
    return _parse_field(field=field, min_value=0, max_value=59)


def parse_hours_field(field: str) -> List[int]:
    return _parse_field(field=field, min_value=0, max_value=23)


def parse_days_of_month_field(field: str) -> List[int]:
    return _parse_field(field=field, min_value=1, max_value=31)


def parse_months_field(field: str) -> List[int]:
    return _parse_field(field=field, min_value=1, max_value=12)


def parse_days_of_week_field(field: str) -> List[int]:
    return _parse_field(field=field, min_value=1, max_value=7)


def parse_command_field(field: str) -> str:
    return field


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
    schedule = parse_cron_string(args.cron_string)
    print(schedule)

