#MainProg by Matthew Rothman
#import functions
import myLib
#read from rumbers, open, and clsoe
infile = 'Rumbers.txt'
f = open(infile,'r')
data = f.read()
f.close()


#make the data into a iterable list
data = data.replace('\n','\t')
data = data.split('\t')

#make harshout a carrier for the return of harshard numbers with sevens to later write to a txtile
harshout = []
total = 0

#find all the harshad number
for num in data:
#convert to ints so that it can be iterated
    if myLib.isHarshad(int(num)):
        total += (int(num))
print(total)
#find all the harshads with seven in the tens place
for num in data:
    if myLib.isSiete(int(num)) and myLib.isHarshad(int(num)) == True:
        harshout.append(num)
        print(num)
      
#find all the harshads with sevens in the tens place divisible by hodges
for num in data:
    if myLib.isSiete(int(num)) and myLib.isHarshad(int(num)) and (int(num)) % myLib.Hodges == 0:
        print(num)

#create harshout file and write the stored values to the txt file
of = open('Harshout.txt', 'w')
for line in harshout:
        of.write(str(line + '\n'))
of.close()
