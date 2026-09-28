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
