TimeInDays = int(input('Please enter the time in days: '))

Years = int(TimeInDays/365)

Months = int((TimeInDays%365)/30)
Days = int((TimeInDays%365)%30)
LeapDays = int(((TimeInDays%365)%30)+ (Years/4))
if Years%4 == 0:
    print('Your conversion is {0} years {1} months {2} days'.format(Years, Months, LeapDays))

else: print('Your conversion is {0} years {1} months {2} days'.format(Years, Months, Days))
