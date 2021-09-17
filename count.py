# build countdown calculator
# take two date input
# calculate time between the two dates
# give dates in format of years:months:weeks:days:hours:minutes:seconds
#string[ start_index_pos: end_index_pos: step_size]
from datetime import  datetime


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

                yearsCalc = lambda x: x/365 if x >= 365 and x%365 == 0 else 0
                mothsCalc = lambda x: x/30.417 if x < 365 and x%12 == 0 else 0
                weeksCalc = lambda x: x/52.1429 if x < 365 else 0


                years = yearsCalc(timeInt)
                months = mothsCalc(timeInt)
                weeks = weeksCalc(timeInt)

                print(f'time that has passed: {int(years)} years:{int(months)} months:{int(weeks)} weeks')













