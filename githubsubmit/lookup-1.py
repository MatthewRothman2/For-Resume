#lookup.py by Matthew Rothman
#import library
import mySearches
#read from file open and close
infile = 'rands.txt'
f = open(infile,'r')
data = f.read()
f.close()
#clean data to make it a comma separated list
data = data.replace('\n','\t')
data = data.split('\t')

#sort data
data.sort()
#create a list to store data in to later append
list2 = []
#append list to integers and sort it for the bsearch and lsearch
for z in data:
    list2.append(int(z))
    list2.sort()


#run both lsearch and bsearch
print((mySearches.bsearch(78700,list2)))
print((mySearches.lsearch(78700,list2)))

print((mySearches.bsearch(3333,list2)))
print((mySearches.lsearch(3333,list2)))

print((mySearches.bsearch(1118,list2)))
print((mySearches.lsearch(1118,list2)))


#input number to search    
z = int(input("Enter Z variable to search"))
print((mySearches.bsearch(z,list2)))
print((mySearches.lsearch(z,list2)))










    





