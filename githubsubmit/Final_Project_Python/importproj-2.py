from finalproject import genre   #import classes
from finalproject import discography  

genre1 = genre(1,2,3,4) #create object


print(genre1.getgenre(genre1.gettitle(),genre1.getmetascore()),genre1.gettitle(),genre1.getmetascore(),genre1.getuserscore())
artist1 = discography(1,2,3,4,5) #create object



#artist1.gettitle demonstration of inheritance since this run through the discography class and inherits the genre attributes
print(artist1.gettitle(),artist1.getartist(),artist1.getalbums(),artist1.getmetascores(),artist1.getusersscore())

print(artist1.stackpop())
