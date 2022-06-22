#Matthew Rothman Poolballs and pool table unit 5 assignment 1
#Python Metholodolgies
#12/2/201
#professor Sorenson
#initate class
class ball():
   
  
    #define ball pts on table and intialize variables
    loc1 = (0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1)
    loc2 = (0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2)
    def __init__(self,number,color,isStriped,location):
        self.number = number
        self.color = color
        self.location = location
        self.loc1 = .5
        self.loc2 = .5
        self.loc3 = 1
        self.loc4 = 2
        self.loc5 = 3
        self.loc6 = 4
        self.isStriped = isStriped
        
    
        
      #return solid or striped if 0 or 1  

    def getisStriped(self):
        if self.isStriped == 0:
            return "striped"
        elif self.isStriped == 1:
            return "solid"

    def getnumber(self):                #return number for object
        return self.number

    def setnumber(self,number):
        self.number = number

    def getcolor(self):         #return color of object
        return self.color

    def setcolor(self,color):
        self.color = color

    def getlocation(self):                      # if the x coor is greater than 1 or less than 0 set to .5.5, else return coor
        if self.loc1 < 0 or self.loc1 > 1:
            return (.5,.5)
        if self.loc2 < 0 or self.loc2 > 2:
            return (.5,.5)
        return (self.loc1,self.loc2)
  
    def getdistance(self):
        distance_from = ((((self.loc5 - self.loc3) ** 2) + (self.loc6 - self.loc4) ** 2) **.5)      #find distance between two balls
        return distance_from

    def setlocation(self,x,y):              #set new location given the coordinate when object is printed
        if x < 0 or x > 1:
            return                          #do nothing if out of bounds
        if y < 0 or y > 2:
            return 
        return (self.loc1,self.loc2) #use as place holder for when actual coor is given during print statement
        

        
              
    

  
ball9 = ball(9,'yellow',0,()) #create objects 
ball7 = ball(7,'maroon',0,())
print(ball9.getnumber(),ball9.getcolor(),ball9.getisStriped(),ball9.getlocation(),ball9.getdistance(),ball9.setlocation(1,2)) #print object with getlocation and new location set location
print(ball7.getnumber(),ball7.getcolor(),ball7.getisStriped(),ball7.getlocation(),ball9.getdistance(),ball9.setlocation(3,4))



