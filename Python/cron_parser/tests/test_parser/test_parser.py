from cron_parser.parser import (
    parse_minutes_field,
    parse_hours_field,
    parse_days_of_month_field,
    parse_months_field,
    parse_days_of_week_field,
    parse_command_field,
    parse_cron_string,
    CronSchedule
)


def test_parse_minutes_field() -> None:
    assert parse_minutes_field(input="1") == [1]
    assert parse_minutes_field(input="1-5") == [1, 2, 3, 4, 5]
    assert parse_minutes_field(input="*") == list(range(1, 61))


def test_parse_hours_field() -> None:
    assert parse_hours_field(input="1") == [1]
    assert parse_hours_field(input="1-5") == [1, 2, 3, 4, 5]
    assert parse_hours_field(input="*") == list(range(1, 25))


def test_parse_days_of_months_field() -> None:
    assert parse_days_of_month_field(input="1") == [1]
    assert parse_days_of_month_field(input="1-5") == [1, 2, 3, 4, 5]
    assert parse_days_of_month_field(input="*") == list(range(1, 32))


def test_parse_months_field() -> None:
    assert parse_months_field(input="1") == [1]
    assert parse_months_field(input="1-5") == [1, 2, 3, 4, 5]
    assert parse_months_field(input="*") == list(range(1, 13))


def test_parse_days_of_week_field() -> None:
    assert parse_days_of_week_field(input="1") == [1]
    assert parse_days_of_week_field(input="1-5") == [1, 2, 3, 4, 5]
    assert parse_days_of_week_field(input="*") == list(range(1, 8))


def test_parse_command_field() -> None:
    assert parse_command_field(input="/usr/bin/find") == "/usr/bin/find"


def test_parse_cron_string_single_value_for_all_fields() -> None:
    assert parse_cron_string(
        cron_string="15 0 1 4 5 /usr/bin/find"
    ) == CronSchedule(
        minutes=[15],
        hours=[0],
        days_of_month=[1],
        months=[4],
        days_of_week=[5],
        command="/usr/bin/find",
    )


def test_parse_cron_string_ranges_for_all_values() -> None:
    assert parse_cron_string(
        cron_string="1-2 2-3 3-4 4-5 5-6 /usr/bin/find"
    ) == CronSchedule(
        minutes=[1, 2],
        hours=[2, 3],
        days_of_month=[3, 4],
        months=[4, 5],
        days_of_week=[5, 6],
        command="/usr/bin/find",
    )


def test_parse_cron_string_wildcards_for_all_values() -> None:
    assert parse_cron_string(
        cron_string="* * * * * /usr/bin/find"
    ) == CronSchedule(
        minutes=list(range(1, 61)),
        hours=list(range(1, 25)),
        days_of_month=list(range(1, 32)),
        months=list(range(1, 13)),
        days_of_week=[1, 2, 3, 4, 5, 6, 7],
        command="/usr/bin/find",
    )
