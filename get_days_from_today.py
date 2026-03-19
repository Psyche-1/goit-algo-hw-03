from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Function return difference between date and today.
    Get string in format 'YYYY-MM-DD'.
    """
    # today_date = datetime(2021, 5, 5)  # 157
    today_date = datetime.now()

    try:
        this_date = datetime.strptime(date, "%Y-%m-%d")
        difference = this_date - today_date
        return difference.days
    except ValueError:
        return 0


# print(get_days_from_today("2021-10-09"))
