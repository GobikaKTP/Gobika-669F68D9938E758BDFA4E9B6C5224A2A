#Leap Year 

def isLeapYear(year):
  if(year % 4 == 0 and year % 100 != 0):
    return True
  elif(year % 400 == 0):
    return True
  else:
    return False

year = int(input("Enter the year: "))

if isLeapYear(year):
  print("{} is a Leap Year.".format(year))
else:
  print("{} is not a Leap Year.".format(year)) 