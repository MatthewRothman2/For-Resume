#Unit Two assignment one Matthew Rothman

#establish the range of i
for i in range (1,101):
#if the number is divisble by 3 and 7 evenly return cowpie
    if i % 7 == 0 and i % 3 == 0:
        print('CowPie')
    elif i % 3==0:
        print('cow')
#if the number is divisble by 7 evenly return pie
    elif i % 7 == 0:
        print('Pie')
#if the number is divisble by 3 
#if none of the above conditions are ture return i 
    else:
        print(i)

