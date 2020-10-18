def quarter_of(month):
    if 10 <= month <= 12:
        return 4
    elif 7 <= month <= 9:
        return 3
    elif 4 <= month <= 6:
        return 2
    else:
        return 1


# Instructions
#
#
#     Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
#
#     For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
