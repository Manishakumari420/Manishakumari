#Leap Year

#year % 4 ==0
#year % 100!=0
#year % 400 ==0


def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year:"))

if isLeapYear(year):
  print((year), "is a Leap year")
else:
  print((year), "is not a Leap year")
