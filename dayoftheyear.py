input_date = "2020-03-01"

def calculate_day_of_the_year(input_date):
    global days_count
    global year
    date_split = input_date.split("-")

    # Getting the year, month and day from the input string
    year = int(date_split[0])
    months = int(date_split[1])
    day = int(date_split[2])

    # The number of days in each month of the year 0-indexed
    total_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    non_leap = 28
    days_count = day

    # Iterating over every month in total_months for every month in the months variable
    for month in total_months[:months]:
        if month != non_leap:
            days_count += int(month)
        # Checking if the year is a leap year or not, if it is then add one day to february
        elif month == non_leap and year % 4 == 0:
            days_count += month + 1

        else:
            days_count += month

calculate_day_of_the_year(input_date)

# Printing the year and the day number for the given input day
print("The input date is {}th day of the year {}".format(days_count, year))