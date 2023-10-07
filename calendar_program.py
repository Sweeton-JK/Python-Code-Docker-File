import calendar
import sys

if len(sys.argv) != 3:
    print("Usage: python calendar_program.py <year> <month>")
    sys.exit(1)

year = int(sys.argv[1])
month = int(sys.argv[2])

if 1 <= month <= 12:
    cal = calendar.month(year, month)
    print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
    print(cal)
else:
    print("Invalid month input. Please enter a month between 1 and 12.")
