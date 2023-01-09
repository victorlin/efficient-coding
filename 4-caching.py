import datetime
import pandas as pd


def read_metadata():
    return pd.read_csv("data/metadata-300k.tsv", sep='\t', usecols=['date'])


def convert_datetime(date):
    """Convert date string into a date object. Only works for format YYYY-MM-DD."""
    try:
        return datetime.date.fromisoformat(date)
    except ValueError:
        return None


if __name__ == "__main__":
    metadata = read_metadata()

    # Filter out un-parse-able date strings.
    dates = [date for date in metadata['date'].apply(convert_datetime) if date]

    print('Date range:', max(dates) - min(dates))


# Profiling shows that convert_datetime is being called 300k times.
# Since there are 300k data points over a 3 year period, there must be many
# repeated conversions.
#
# from functools import lru_cache
# set @lru_cache above get_datetime
