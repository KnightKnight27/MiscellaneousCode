from cron_parser.parser import parse_cron_string, CronSchedule

"""
*/15 0 1,15 * 1-5 /usr/bin/find

Should yield the following output:

minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find

"""


def test_singe_value_for_all_fields() -> None:
    assert parse_cron_string(
        "15 0 1 4 5 /usr/bin/find"
    ) == CronSchedule(
        minutes=[15],
        hours=[0],
        days_of_month=[1],
        months=[4],
        days_of_week=[5],
        command="/usr/bin/find",
    )
