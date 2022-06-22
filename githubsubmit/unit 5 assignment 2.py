#Matthew Rothman Unit 5 assignment 2
#Python Metholdogies
#12/2/2021
#Professor Sorenson

#import random for randomization of ball locations
import random

class ball():
    #lists to append later
    distances = []
    mindistance = []

   
    def __init__(self,number,color,isStriped,location,distance):
        self.number = number
        self.color = color
        self.location = location
        self.isStriped = isStriped
        self.distance = distance
        self.loc1 = (0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1)
        self.loc2 = (0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2)
        self.loc3 = random.choice(self.loc1) #randomize x and y coor
        self.loc4 = random.choice(self.loc2)
        
        

    def getisStriped(self):
        if self.isStriped == 0:
            return "striped"
        elif self.isStriped == 1:
            return "solid"

    def getnumber(self):
        return self.number

    def setnumber(self,number):
        self.number = number

    def getcolor(self):
        return self.color

    def setcolor(self,color):
        self.color = color

    def getlocation(self):
        if self.loc3 < 0 or self.loc3 > 1:  #if less than 0 or greater than 1 or less than 0 or greater than 2 return .5,.5
            return (.5,.5)
        if self.loc4 < 0 or self.loc4 > 2:
            return (.5,.5)
        else:
            return(self.loc3,self.loc4)
   
            
    def setlocation(self):
            if self.loc3 < 0 or self.loc3 > 1:   #if less than 0 or greater than 1 or less than 0 or greater than 2 return .5,.5
                return 
            elif self.loc4 < 0 or self.loc4 > 2:
                return 
            else:
                return(self.loc3,self.loc4)
            
    def getdistance(self,getlocation):
        distance_from = ((((self.loc3 - ball9.loc3) ** 2) + (self.loc4 - ball9.loc4) ** 2) **.5)   #distances between ball 9 and random pts
        return distance_from

    def getdistances(self,getlocation):
        distance_from = ((((self.loc3 - ball9.loc3) ** 2) + (self.loc4 - ball9.loc4) ** 2) **.5) #use for append list
        return distance_from

    def closesthole(self):
        hole1 = ((((0 - ball9.loc3) ** 2) + (0 - ball9.loc4) ** 2) **.5)
        hole2 = ((((0 - ball9.loc3) ** 2) + (1 - ball9.loc4) ** 2) **.5)            #all holes lcoations compared to hole 9
        hole3 = ((((0 - ball9.loc3) ** 2) + (2 - ball9.loc4) ** 2) **.5)
        hole4 = ((((1 - ball9.loc3) ** 2) + (0 - ball9.loc4) ** 2) **.5)
        hole5 = ((((1 - ball9.loc3) ** 2) + (1 - ball9.loc4) ** 2) **.5)
        hole6 = ((((1 - ball9.loc3) ** 2) + (2 - ball9.loc4) ** 2) **.5)
        
        return hole1,hole2,hole3,hole4,hole5,hole6


ball1 = ball(1,'yellow',1,(.4,.4),1)            #create all balls
ball2 = ball(2,'blue',1,(.4,.4),1)
ball3 = ball(3,'red',1,(.4,.4),1)
ball4 = ball(4,'violet',1,(.4,.4),1)
ball5 = ball(5,'orange',1,(.4,.4),1)
ball6 = ball(6,'green',1,(.4,.4),1)
ball7 = ball(7,'maroon',1,(.4,.4),1)
ball8 = ball(8,'black', 1, (.4,.4),1)
ball9 = ball(9,'yellow',0,(.4,.4),1)
ball10 = ball(10,'blue',0,(.4,.4),1)
ball11 = ball(11,'red',0,(.4,.4),1)
ball12 = ball(12,'violet', 0, (.4,.4),1)
ball13 = ball(13,'orange',0,(.4,.4),1)
ball14 = ball(14,'green',0,(.4,.4),1)
ball15 = ball(15,'maroon',0,(.4,.4),1)
cueball = ball(16,'white',1,(.4,.4),1)

ball.distances.append(ball1.getnumber())
ball.distances.append(ball1.getdistances(ball9.getlocation()))      #append number and distance to the list
ball.distances.append(ball2.getnumber())
ball.distances.append(ball2.getdistances(ball9.getlocation()))
ball.distances.append(ball3.getnumber())
ball.distances.append(ball3.getdistances(ball9.getlocation()))
ball1.distances.append(ball4.getnumber())
ball.distances.append(ball4.getdistances(ball9.getlocation()))
ball1.distances.append(ball5.getnumber())
ball.distances.append(ball5.getdistances(ball9.getlocation()))
ball1.distances.append(ball6.getnumber())
ball.distances.append(ball6.getdistances(ball9.getlocation()))
ball1.distances.append(ball7.getnumber())
ball.distances.append(ball7.getdistances(ball9.getlocation()))
ball1.distances.append(ball8.getnumber())
ball.distances.append(ball8.getdistances(ball9.getlocation()))
ball1.distances.append(ball10.getnumber())
ball.distances.append(ball10.getdistances(ball9.getlocation()))
ball1.distances.append(ball11.getnumber())
ball.distances.append(ball11.getdistances(ball9.getlocation()))
ball1.distances.append(ball12.getnumber())
ball.distances.append(ball12.getdistances(ball9.getlocation()))
ball1.distances.append(ball13.getnumber())
ball.distances.append(ball13.getdistances(ball9.getlocation()))
ball1.distances.append(ball4.getnumber())
ball.distances.append(ball14.getdistances(ball9.getlocation()))
ball1.distances.append(ball5.getnumber())
ball.distances.append(ball15.getdistances(ball9.getlocation()))
ball1.distances.append(cueball.getnumber())
ball.distances.append(cueball.getdistances(ball9.getlocation()))






ball.mindistance.append(min(ball.distances))            #print the closest distance to the 9 ball
print("closest ball to ball 9",ball.mindistance)



print(ball1.getnumber(),ball1.getcolor(),ball1.getisStriped(),ball1.getlocation(), ball1.getdistance(ball9.getlocation()), ball1.setlocation())
print(ball2.getnumber(),ball2.getcolor(),ball2.getisStriped(),ball2.getlocation(), ball2.getdistance(ball9.getlocation()), ball2.setlocation())     #print all attributes
print(ball3.getnumber(),ball3.getcolor(),ball3.getisStriped(),ball3.getlocation(), ball2.getdistance(ball9.getlocation()), ball3.setlocation())
print(ball4.getnumber(),ball4.getcolor(),ball4.getisStriped(),ball4.getlocation(), ball4.getdistance(ball9.getlocation()), ball4.setlocation())
print(ball5.getnumber(),ball5.getcolor(),ball5.getisStriped(),ball5.getlocation(), ball5.getdistance(ball9.getlocation()), ball5.setlocation())
print(ball6.getnumber(),ball6.getcolor(),ball6.getisStriped(),ball6.getlocation(), ball6.getdistance(ball9.getlocation()), ball6.setlocation())
print(ball7.getnumber(),ball7.getcolor(),ball7.getisStriped(),ball7.getlocation(), ball7.getdistance(ball9.getlocation()), ball7.setlocation())
print(ball8.getnumber(),ball8.getcolor(),ball8.getisStriped(),ball8.getlocation(), ball8.getdistance(ball9.getlocation()), ball8.setlocation())
print(ball9.getnumber(),ball9.getcolor(),ball9.getisStriped(),ball9.getlocation(), ball9.setlocation())
print(ball10.getnumber(),ball10.getcolor(),ball10.getisStriped(),ball10.getlocation(), ball10.getdistance(ball9.getlocation()), ball10.setlocation())
print(ball11.getnumber(),ball11.getcolor(),ball11.getisStriped(),ball11.getlocation(), ball11.getdistance(ball9.getlocation()), ball11.setlocation())
print(ball12.getnumber(),ball12.getcolor(),ball12.getisStriped(),ball12.getlocation(), ball12.getdistance(ball9.getlocation()), ball12.setlocation())
print(ball13.getnumber(),ball13.getcolor(),ball13.getisStriped(),ball13.getlocation(), ball13.getdistance(ball9.getlocation()), ball13.setlocation())
print(ball14.getnumber(),ball14.getcolor(),ball14.getisStriped(),ball14.getlocation(), ball14.getdistance(ball9.getlocation()), ball14.setlocation())
print(ball15.getnumber(),ball15.getcolor(),ball15.getisStriped(),ball15.getlocation(), ball15.getdistance(ball9.getlocation()), ball15.setlocation())
print(cueball.getnumber(),cueball.getcolor(),cueball.getisStriped(),cueball.getlocation(), cueball.getdistance(ball9.getlocation()), cueball.setlocation())
print("closest hole distance to ball9",(min(ball9.closesthole())))  #print closest hole distanc to nine



