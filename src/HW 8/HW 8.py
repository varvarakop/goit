from datetime import datetime, timedelta


current_datetime = datetime.now()
current_date1 = current_datetime.date()

one_day = timedelta(days=1)
two_days = timedelta(days=2)
three_days = timedelta(days=3)
four_days = timedelta(days=4)
five_days = timedelta(days=5)
six_days = timedelta(days=6)
seven_days = timedelta(days=7)

current_datetime2 = current_datetime+one_day
current_date2 = current_datetime2.date()

current_datetime3 = current_datetime+two_days
current_date3 = current_datetime3.date()

current_datetime4 = current_datetime+three_days
current_date4 = current_datetime4.date()

current_datetime5 = current_datetime+four_days
current_date5 = current_datetime5.date()

current_datetime6 = current_datetime+five_days
current_date6 = current_datetime6.date()

current_datetime7 = current_datetime+six_days
current_date7 = current_datetime7.date()

current_datetime8 = current_datetime+seven_days
current_date8 = current_datetime8.date()

d1 = datetime(year=2001, month=5, day=27)
d1_d = d1.date()

d2 = datetime(year=2002, month=5, day=28)
d2_d = d2.date()

d3 = datetime(year=2001, month=5, day=29)
d3_d = d3.date()

d4 = datetime(year=2000, month=5, day=30)
d4_d = d4.date()

d5 = datetime(year=2001, month=5, day=31)
d5_d = d5.date()

d6 = datetime(year=2001, month=6, day=1)
d6_d = d6.date()

d7 = datetime(year=1991, month=6, day=2)
d7_d = d7.date()

users = [{'name': 'Vasya', 'birthday': d1_d},
         {'name': 'Kolya', 'birthday': d2_d}, {'name': 'Dasha', 'birthday': d3_d}, {'name': 'Pasha', 'birthday': d4_d}, {'name': 'Vitya', 'birthday': d5_d}, {'name': 'Polya', 'birthday': d6_d}, {'name': 'Dima', 'birthday': d7_d}]


def get_birthdays_per_week(users):

    users_birthdays1 = ['Monday', ]
    users_birthdays2 = ['Tuesday', ]
    users_birthdays3 = ['Wednesday']
    users_birthdays4 = ['Thursday', ]
    users_birthdays5 = ['Friday', ]
    users_birthdays6 = [
        f'Saturday (Congratulations on Monday {current_date8})', ]
    users_birthdays7 = [
        f'Sunday (Congratulations on Monday {current_date8})', ]
    for user in users:
        for _, value in user.items():
            if current_date1.day == user.get('birthday').day and current_date1.month == user.get('birthday').month:
                users_birthdays1.append(value)
            if current_date2.day == user.get('birthday').day and current_date2.month == user.get('birthday').month:
                users_birthdays2.append(value)
            if current_date3.day == user.get('birthday').day and current_date3.month == user.get('birthday').month:
                users_birthdays3.append(value)
            if current_date4.day == user.get('birthday').day and current_date4.month == user.get('birthday').month:
                users_birthdays4.append(value)
            if current_date5.day == user.get('birthday').day and current_date5.month == user.get('birthday').month:
                users_birthdays5.append(value)
            if current_date6.day == user.get('birthday').day and current_date6.month == user.get('birthday').month:
                users_birthdays6.append(value)
            if current_date7.day == user.get('birthday').day and current_date7.month == user.get('birthday').month:
                users_birthdays7.append(value)

    return [users_birthdays1, users_birthdays2, users_birthdays3, users_birthdays4, users_birthdays5, users_birthdays6, users_birthdays7]


print(get_birthdays_per_week(users))