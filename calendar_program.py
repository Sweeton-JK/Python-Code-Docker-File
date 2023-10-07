import calendar

year = int(input("Enter year (e.g., 2023): "))
month = int(input("Enter month (1-12): "))

if 1 <= month <= 12:
    cal = calendar.month(year, month)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(cal)
else:
    print("Invalid month input. Please enter a month between 1 and 12.")
