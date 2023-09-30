#program to display futhure leap year from current year to a final year entered by user
currentyear=int(input("enter the current year:"))
finalyear=int(input("enter the final year:"))
for year in range(currentyear,finalyear+1,1):
    if (year%4==0and year%100!=0) or (year%100==0 and year%400==0):
        print("the year is leap year",year)
    else:
        print("the year is not a leap year",year)
                       
