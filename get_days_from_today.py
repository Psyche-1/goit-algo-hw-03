from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Function return difference between date and today.
    Get string in format 'YYYY-MM-DD'.
    """
    # today_date = datetime(2021, 5, 5).date()  # 157
    today_date = datetime.today().date()

    try:
        this_date = datetime.strptime(date, "%Y-%m-%d").date()
        difference = this_date - today_date
        return difference.days
    except ValueError:
        return None


# print(get_days_from_today("2021-10-09"))
