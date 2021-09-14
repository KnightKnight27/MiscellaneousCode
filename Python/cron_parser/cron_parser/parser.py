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

    @staticmethod
    def _list_to_str(the_list: List):
        return " ".join([str(x) for x in the_list])

    def __repr__(self):
        return "\n".join([
            f"{'minute':14} {self._list_to_str(self.minutes)}",
            f"{'hour':14} {self._list_to_str(self.hours)}",
            f"{'day of month':14} {self._list_to_str(self.days_of_month)}",
            f"{'month':14} {self._list_to_str(self.months)}",
            f"{'day of week':14} {self._list_to_str(self.days_of_week)}",
            f"{'command':14} {self.command}",
        ])


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
    parser = argparse.ArgumentParser(
        description="Parse cron string and print out field values"
    )

    parser.add_argument(
        "cron_string", type=str, help="Input string in cron format"
    )

    args = parser.parse_args()
    schedule = parse_cron_string(args.cron_string)
    print(schedule)
