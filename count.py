# build countdown calculator
# take two date input
# calculate time between the two dates
# give dates in format of years:months:weeks:days:hours:minutes:seconds
#string[ start_index_pos: end_index_pos: step_size]
from datetime import  datetime
import math


def countDown(startDate = input("Insert start date month/day/year:"), enddate = input("Insert end date month/day/year:")):
        sYear = int(startDate[6::])
        sMonth = int(startDate[0:2])
        sDay = int(startDate[3:5])
        start = datetime(sYear, sMonth, sDay)

        eYear = int(enddate[6::])
        eMonth = int(enddate[0:2])
        eDay = int(enddate[3:5])
        end = datetime(eYear, eMonth, eDay)

        if start.date() <= end.date():
                timeElapsed = end.date() - start.date()
                timeInt = int(timeElapsed.days)
                years = 0


                while timeInt >=365:
                        timeInt -= 1
                        if timeInt%365 == 0:
                                years += 1
                                continue
                while timeInt >=30:
                        timeInt /=30.417
                months = math.floor(timeInt)
                print(f'it has been {years} years and {months} months from {start.date()} to {end.date()}')
                return f'it has been {years} and {months} from {start} to {end}'


















