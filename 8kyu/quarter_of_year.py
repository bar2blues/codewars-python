def quarter_of(month):
    if 10 <= month <= 12:
        return 4
    elif 7 <= month <= 9:
        return 3
    elif 4 <= month <= 6:
        return 2
    else:
        return 1