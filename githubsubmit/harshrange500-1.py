#harshad function by Matthew Rothman
#define function
def isHarshad(num):
    total = 0
    #convert to string to make invidual digits
    for digit in str(int(num)):
        #add those digits together to get sum
        total += (int(digit))
    #divide the orig num by the total digits
    if num % (total) == 0:
        return True
    else:
        return False
print(isHarshad(188))

#take a range of 1 to 501 and return true if the function is true
for i in range(1,501):
    if isHarshad(i) == True:
        print(i)

    
    
           
