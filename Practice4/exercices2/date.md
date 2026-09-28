# Dates and time

The `datetime` module provides `date`, `time`, `datetime`, `timedelta`, and `timezone` objects.

```python
from datetime import datetime, timedelta, timezone

start = datetime(2026, 9, 1, 9, 0)
later = start + timedelta(days=2, hours=3)
print(later.strftime("%Y-%m-%d %H:%M"))
print(later - start)

utc_now = datetime.now(timezone.utc)
```

Use `strftime()` to format a date. Subtracting datetimes gives a `timedelta`. Timezone-aware datetimes include an offset and can be converted with `astimezone()`; use UTC when storing or comparing instants across timezones.

## Four date programs

```python
from datetime import date, datetime, timedelta

# 1. Subtract five days from today's date.
today = date.today()
print("Five days ago:", today - timedelta(days=5))

# 2. Print yesterday, today, and tomorrow.
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

# 3. Drop microseconds from the current datetime.
current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)
print("Without microseconds:", without_microseconds)

# 4. Calculate the difference between two datetimes in seconds.
first = datetime(2026, 9, 1, 9, 0, 0)
second = datetime(2026, 9, 3, 12, 30, 0)
difference_seconds = abs((second - first).total_seconds())
print("Difference in seconds:", int(difference_seconds))
```
