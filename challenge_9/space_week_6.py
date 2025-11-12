from datetime import datetime


def moon_phase(date_string):
    ref_date = datetime(2000, 1, 6)
    date = datetime.strptime(date_string, "%Y-%m-%d")

    days_diff = (date - ref_date).days

    cycle_day = (days_diff % 28) + 1

    if 1 <= cycle_day <= 7:
        return "New"
    elif 8 <= cycle_day <= 14:
        return "Waxing"
    elif 15 <= cycle_day <= 21:
        return "Full"
    else:
        return "Waning"



print(moon_phase("2000-01-12"))
print(moon_phase("2000-01-13"))
print(moon_phase("2014-10-15"))
print(moon_phase("2012-10-21"))
print(moon_phase("2022-12-14"))
