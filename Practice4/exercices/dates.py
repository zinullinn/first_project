"""Date and time operations for Practice 4."""

from datetime import date, datetime, timedelta, timezone


def main() -> None:
    today = date.today()
    now = datetime.now()

    print("five days ago:", today - timedelta(days=5))
    print("yesterday:", today - timedelta(days=1))
    print("today:", today)
    print("tomorrow:", today + timedelta(days=1))
    print("datetime without microseconds:", now.replace(microsecond=0))

    first_date = datetime(2026, 9, 1, 9, 0, 0)
    second_date = datetime(2026, 9, 3, 12, 30, 0)
    difference_seconds = abs((second_date - first_date).total_seconds())
    print("date difference in seconds:", int(difference_seconds))

    appointment = datetime(2026, 10, 15, 14, 30)
    print("appointment:", appointment)
    print("formatted:", appointment.strftime("%A, %B %d, %Y at %I:%M %p"))

    start = datetime(2026, 9, 1, 9, 0)
    finish = datetime(2026, 9, 3, 12, 30)
    difference = finish - start
    print("time difference:", difference.days, "days and", difference.seconds // 3600, "hours")
    print("one week after start:", (start + timedelta(weeks=1)).isoformat(sep=" "))

    # Aware datetimes represent instants. UTC+5 is the local offset used in this example.
    oral_time = datetime(2026, 9, 29, 12, 0, tzinfo=timezone(timedelta(hours=5)))
    print("Oral time:", oral_time.isoformat())
    print("same instant in UTC:", oral_time.astimezone(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
