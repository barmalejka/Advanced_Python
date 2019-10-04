import operator
from datetime import datetime, timedelta


def count_entries():
    while True:
        try:
            counter = int(input("Enter number of terms: "))
        except ValueError:
            print('Should be a positive integer number. Please try again.')
            continue
        if counter < 2:
            print("Operation can't be performed on less than 2 numbers")
            continue
        else:
            break
    return counter


def enter_date():
    while True:
        date = input('Enter first term: ')
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("First term should be a date in yyyy-mm-dd format. Please try again.")
            continue
        else:
            break
    return date


def evaluate_dates(dates, operation):
    start_date = dates.pop(0)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        }

    for i in range(len(dates)):
        try:
            result = operations[operation[i]](start_date, timedelta(days=dates[i]))
        except OverflowError:
            result = 'Numbers added/subtracted are to big'
            break
        start_date = result

    if not isinstance(result, str):
        result = result.strftime('%Y-%m-%d')

    return result