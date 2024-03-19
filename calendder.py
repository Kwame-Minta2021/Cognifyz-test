import calendar

def display_calendar():
    # Get user input for the year
    year = int(input("Enter the year you want to view the calendar for: "))

    # Create a TextCalendar object
    cal = calendar.TextCalendar(calendar.SUNDAY)

    # Loop through each month and display the calendar
    for month in range(1, 13):
        # Get the calendar for the month
        month_calendar = cal.formatmonth(year, month)
        print(month_calendar)

# Example usage: Display calendar for the year entered by the user
display_calendar()
