# Matthew Rothman's measurement converter
# the goal of this program is to be able to convert inches to feet, yards,
# and miles

#Enter in the number of inches that needs to be converted

inches = int(input("Enter inches: "))

#inches divided by 12 will result in x amount of feet
feet = inches//12

print(feet)

#inches divided by 12 then divded by 3 will result in x amount of yards

yards = (inches//12)/3

print(yards)

#yards divided by 1760 will result in the number of miles

miles = (yards//1760)

print(miles)
