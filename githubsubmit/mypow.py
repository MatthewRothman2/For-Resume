#myPow by Matthew Rothamn

#define fucntion two variables
def myPow(x,y):
#since exponents set to 0 = 1 return 1 if this happens
    if y == 0:
        return 1
#else run recursive exponential function that multiple into itself based on the exponent
    else:
        return x * myPow(x,y-1)
#input base and exponent
x = int(input("enter value for base 'x'"))
y = int(input("enter value for exponenet 'y'"))
#print
print(myPow(x,y))
    
