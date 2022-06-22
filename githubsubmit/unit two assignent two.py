#assignment two Matthew Rothman
#Establish the list
mylist = [23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45,
          93, -43, 999, -2, 3, 78, 90]
#create variables for future use for counter and total
c = 0
a = 0
#Python will pull from the list and then stop when it hits 999
for i in mylist:
    if i == 999:
        break
#if the number is less than 0 python will return it
    if i < 0:
#c is the counter and a is the total
        c = c + 1
        a = a + i
#print the total divded by the number of items in the list
print(a/c)
            
            
           
#Created these two lists to see what the total of the number before 999 were
#therefore I can see if the code is pulling just the negatives or both positives
#and negatives
#sum of negatives before 999 is -202 and there are 8 negatives
#in which case -202/8 = approx -25.25
'''
lists = [23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45,
          93, -43]
print(sum(lists))


secondlists = [-45,-23,-9,-54,-2,-3,-23,-43]
print(sum(secondlists))
'''
