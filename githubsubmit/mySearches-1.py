#Matthew Rothman Python Methodologies
#attributed Professor Sorenson
#Define Bsearch

def bsearch(number, list_nums):                   # set the item and low point to Zero
    item =0
    low = 0                             #python counts from 0 so need to reduce length by one
    high = len(list_nums) -1
    c = 0
    while low <= high:                 #While low is <= to high print stepcounter get new mid point             
        print("Step counter : ",c,item)
        mid = (low+high)//2     #finding middle point
        item = list_nums[mid]
        print("The Mid:",item)
        if number == item:            #If x = item print the item
            c = c + 1
            return mid
        elif number < item:           #if x is less than item move the mid point down one and divide again
            high = mid -1    
            c = c + 1        
        else:                
            low = mid + 1    
            c = c + 1        
    return -1                #if not found return negative 1
####
# Linear search
def lsearch(number, list_nums):   #Define two variables one is the range, other is searchable item 
    c = 0
    for i in range(0,len(list_nums)-1): #create range
        if number == list_nums[i]:  #x = equals of the number being searched
            c = c + 1
            print("Number Found!",i)
            print("Linear Search took",c,"passes\n")
            return i
        else:
            c = c + 1
            
    print("Number not found")
    print("The Search took",c,"passes\n")
    return -1 #if not found return -1
#####
'''
ints = (list(range(1,1000000)))
# print(MyNums[4])
x = bsearch(2000,ints)
print(x)
print("The number is found! : ", ints[x],'\n')

x = lsearch(1,ints)
print(x)
'''
