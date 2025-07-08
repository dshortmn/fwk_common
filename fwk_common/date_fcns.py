import calendar
from datetime import datetime, timedelta, timezone

from dateutil.relativedelta import relativedelta


def week(inDate: datetime):
    """
    Returns the week number of the year for a given date.
    """
    week_number = inDate.isocalendar().week
    start_of_week = inDate - timedelta(days=inDate.weekday())
    days_until_sunday = 6 - inDate.weekday()
    end_of_week = inDate + timedelta(days=days_until_sunday)
    if inDate < start_of_week or inDate > end_of_week:
        # If the date is outside the current week, return the week number
        # of the start of the week
        start_week_number = start_of_week.isocalendar()[1]
        if start_week_number == 1 and inDate.month == 12:
            # If the start of the week is in December, return week 53
            return 53
        elif start_week_number == 52 and inDate.month == 1:
            # If the start of the week is in January, return week 1
            return 1
        else:
            # Otherwise, return the week number of the start of the week
            week_number = start_week_number
        if week_number == 1 and inDate.month == 12:
            # If the week number is 1 and the month is December, return week 53
            return 53
        elif week_number == 52 and inDate.month == 1:
            # If the week number is 52 and the month is January, return week 1
            return 1
    return week_number, start_of_week, end_of_week


def date_dict():
    """
    Returns a dictionary with the current date in UTC.
    """
    results = {}
    # Get the current date in UTC
    utc_date = datetime.now(timezone.utc)  # Convert to UTC if not already in UTC
    results["curr_date"] = utc_date.strftime("%Y-%m-%d")
    results["curr_day_nr"] = str(utc_date.day).zfill(2)
    results["curr_day_month_nr"] = str(utc_date.month).zfill(2)
    results["curr_day_year_nr"] = str(utc_date.year).zfill(4)
    # Get the previous date
    prev_date = utc_date - timedelta(days=1)
    results["prev_date"] = prev_date.strftime("%Y-%m-%d")
    results["prev_day_nr"] = str(prev_date.day).zfill(2)
    results["prev_day_month_nr"] = str(prev_date.month).zfill(2)
    results["prev_day_year_nr"] = str(prev_date.year).zfill(4)
    # Get the week number and start/end of the week
    week_nr, start_of_week, end_of_week = week(utc_date)
    results["curr_week_nr"] = str(week_nr).zfill(2)
    results["curr_start_of_week"] = start_of_week.strftime("%Y-%m-%d")
    results["curr_end_of_week"] = end_of_week.strftime("%Y-%m-%d")
    results["curr_week_start_day_nr"] = str(start_of_week.day).zfill(2)
    results["curr_week_start_month_nr"] = str(start_of_week.month).zfill(2)
    results["curr_week_start_year_nr"] = str(start_of_week.year).zfill(4)
    results["curr_week_end_day_nr"] = str(end_of_week.day).zfill(2)
    results["curr_week_end_month_nr"] = str(end_of_week.month).zfill(2)
    results["curr_week_end_year_nr"] = str(end_of_week.year).zfill(4)
    # Get the previous week number and start/end of the week
    prev_week = start_of_week - timedelta(days=7)
    prev_week_nr, prev_start_of_week, prev_end_of_week = week(prev_week)
    results["prev_week_nr"] = str(prev_week_nr).zfill(2)
    results["prev_week_start"] = prev_start_of_week.strftime("%Y-%m-%d")
    results["prev_week_end"] = prev_end_of_week.strftime("%Y-%m-%d")
    results["prev_week_start_day_nr"] = str(prev_start_of_week.day).zfill(2)
    results["prev_week_start_month_nr"] = str(prev_start_of_week.month).zfill(2)
    results["prev_week_start_year_nr"] = str(prev_start_of_week.year).zfill(4)
    results["prev_week_end_day_nr"] = str(prev_end_of_week.day).zfill(2)
    results["prev_week_end_month_nr"] = str(prev_end_of_week.month).zfill(2)
    results["prev_week_end_year_nr"] = str(prev_end_of_week.year).zfill(4)
    # Get the current month start and end dates
    curr_month_start = utc_date.replace(day=1)
    last_day = calendar.monthrange(utc_date.year, utc_date.month)[1]
    curr_month_end = utc_date.replace(day=last_day)
    results["curr_month_start"] = curr_month_start.strftime("%Y-%m-%d")
    results["curr_month_end"] = curr_month_end.strftime("%Y-%m-%d")
    results["curr_month_nr"] = str(utc_date.month).zfill(2)
    results["curr_year_nr"] = str(utc_date.year).zfill(4)
    results["curr_year_month"] = utc_date.strftime("%Y-%m")
    # Get the previous month start and end dates
    prev_month_start = curr_month_start - relativedelta(months=1)
    last_day = calendar.monthrange(prev_month_start.year, prev_month_start.month)[1]
    prev_month_end = prev_month_start.replace(day=last_day)
    results["prev_month_start"] = prev_month_start.strftime("%Y-%m-%d")
    results["prev_month_end"] = prev_month_end.strftime("%Y-%m-%d")
    results["prev_month_nr"] = str(prev_month_start.month).zfill(2)
    results["prev_year_nr"] = str(prev_month_start.year).zfill(4)
    results["prev_year_month"] = prev_month_start.strftime("%Y-%m")
    # Get the current year start and end dates
    curr_year_start = utc_date.replace(month=1, day=1)
    curr_year_end = utc_date.replace(month=12, day=31)
    results["curr_year_start"] = curr_year_start.strftime("%Y-%m-%d")
    results["curr_year_end"] = curr_year_end.strftime("%Y-%m-%d")
    # Get the previous year start and end dates
    prev_year_start = utc_date.replace(month=1, day=1) - relativedelta(years=1)
    prev_year_end = utc_date.replace(month=12, day=31) - relativedelta(years=1)
    results["prev_year_start"] = prev_year_start.strftime("%Y-%m-%d")
    results["prev_year_end"] = prev_year_end.strftime("%Y-%m-%d")
    #
    new_items_dict = {
        "nodash_" + key: value.replace("-", "") for key, value in results.items()
    }
    results = results | new_items_dict

    return results
