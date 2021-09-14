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
    assert parse_minutes_field(field="1") == [1]
    assert parse_minutes_field(field="1,2") == [1, 2]
    assert parse_minutes_field(field="1-5") == [1, 2, 3, 4, 5]
    assert parse_minutes_field(field="*") == list(range(0, 60))
    assert parse_minutes_field(field="*/10") == [0, 10, 20, 30, 40, 50]


def test_parse_hours_field() -> None:
    assert parse_hours_field(field="1") == [1]
    assert parse_hours_field(field="1,2") == [1, 2]
    assert parse_hours_field(field="1-5") == [1, 2, 3, 4, 5]
    assert parse_hours_field(field="*") == list(range(0, 24))
    assert parse_hours_field(field="*/6") == [0, 6, 12, 18]


def test_parse_days_of_months_field() -> None:
    assert parse_days_of_month_field(field="1") == [1]
    assert parse_days_of_month_field(field="1,2") == [1, 2]
    assert parse_days_of_month_field(field="1-5") == [1, 2, 3, 4, 5]
    assert parse_days_of_month_field(field="*") == list(range(1, 32))
    assert parse_days_of_month_field(field="*/5") == [1, 6, 11, 16, 21, 26, 31]


def test_parse_months_field() -> None:
    assert parse_months_field(field="1") == [1]
    assert parse_months_field(field="1,2") == [1, 2]
    assert parse_months_field(field="1-5") == [1, 2, 3, 4, 5]
    assert parse_months_field(field="*") == list(range(1, 13))
    assert parse_months_field(field="*/3") == [1, 4, 7, 10]


def test_parse_days_of_week_field() -> None:
    assert parse_days_of_week_field(field="1") == [1]
    assert parse_days_of_week_field(field="1,2") == [1, 2]
    assert parse_days_of_week_field(field="1-5") == [1, 2, 3, 4, 5]
    assert parse_days_of_week_field(field="*") == list(range(1, 8))
    assert parse_days_of_week_field(field="*/2") == [1, 3, 5, 7]


def test_parse_command_field() -> None:
    assert parse_command_field(field="/usr/bin/find") == "/usr/bin/find"


def test_parse_cron_string_single_value_for_all_time_fields() -> None:
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


def test_parse_cron_string_comma_separated_values_for_all_time_fields() -> None:
    assert parse_cron_string(
        cron_string="15,16 0,1 1,2 4,5 5,6 /usr/bin/find"
    ) == CronSchedule(
        minutes=[15, 16],
        hours=[0, 1],
        days_of_month=[1, 2],
        months=[4, 5],
        days_of_week=[5, 6],
        command="/usr/bin/find",
    )


def test_parse_cron_string_ranges_for_all_time_fields() -> None:
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


def test_parse_cron_string_wildcards_for_all_time_fields() -> None:
    assert parse_cron_string(
        cron_string="* * * * * /usr/bin/find"
    ) == CronSchedule(
        minutes=list(range(0, 60)),
        hours=list(range(0, 24)),
        days_of_month=list(range(1, 32)),
        months=list(range(1, 13)),
        days_of_week=[1, 2, 3, 4, 5, 6, 7],
        command="/usr/bin/find",
    )
