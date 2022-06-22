#Final Project by Matthew Rothman
#Python Methodolgies
#Professor Sorenson

import pandas as pd #import pandas as pd to read in excel file



class genre():
    x = (int(input("Minimum score for metacritic reviewed album")))  #input minimum score of metacritic album
    y = (int(input("Minimum score for user reviewed album")))       #input minimum score of user reviewed albumm
    

    def __init__(self,genre,title,metascore,userscore):     #define variables
        self.genre = genre
        self.title = title
        self.metascore = metascore
        self.userscore = userscore
        self.infile = infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')   #define the read file statment in case it needs to be called but for the most part this is a placeholder
        self.genres = (str(input("Genre you would like to view")))  #make genre able to input as a string
        self.titles = (infile['Title'].where(infile['Genre'] == self.genres))    #titles variable to call later
          

    def getgenre(self,x,y):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx') #read statment  
        genre_s = (infile['Genre'].where(infile['Genre'] == self.genres)) #find entered in genre in the excel file and return it without the NaN values
        return genre_s.dropna()#without the NaN values

    def gettitle(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        titles = (infile[('Title')].where(infile['Genre'] == self.genres)) #return titles for entered in genre
        return titles.dropna()#without the NaN values

    def getmetascore(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        metascores = (self.titles.where(infile['Metacritic Critic Score'] >= genre.x)) #return only metascore titles with above the specified rating
        return metascores.dropna()#without the NaN values

    def getuserscore(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        userscore = (self.titles.where(infile['Metacritic User Score'] >= genre.y)) #return only user titles with above the specified rating
        return userscore.dropna()#without the NaN values

    




class discography(genre):
    def __init__(self,artist,albums,meta,user,stackpop):
        genre.__init__(self,genre,albums,meta,user)
        self.artist = (str(input("Artist Discogrpahy you would like to view"))) #artist that you would like to search
        self.albums = albums
        self.infile = infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        self.x = (int(input("Minimum score for metacritic reviewed album"))) #input minimum score of metacritic album
        self.y = (int(input("Minimum score for user reviewed album")))#input minimum score of user reviewed albumm
        self.alb = (infile[('Title')].where(infile['Artist'] == self.artist))
        self.artists = (infile['Artist'].where(infile['Artist'] == self.artist))
        self.users = users = (self.alb.where(infile['Metacritic User Score'] >= self.y))
        
    def getartist(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        artists = (infile['Artist'].where(infile['Artist'] == self.artist)) #return artist based on artist entered
        return artists.dropna()


    def getalbums(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        alb = (infile[('Title')].where(infile['Artist'] == self.artist)) #return titles of the artist
        return alb.dropna() #without the NaN values

    def getmetascores(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        metascores = (self.alb.where(infile['Metacritic Critic Score'] >= self.x)) #return only metascore titles with above the specified rating
        return metascores.dropna()#without the NaN values

    def getusersscore(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        users = (self.alb.where(infile['Metacritic User Score'] >= self.y))#return only user titles with above the specified rating
        return users.dropna()#without the NaN values

    def stackpop(self):
        infile = pd.read_excel(r'C:\Users\mattr\OneDrive\Desktop\Python\albums.xlsx')#read statment
        users = (self.alb.where(infile['Metacritic User Score'] >= self.y)) 
        metascores = (self.alb.where(infile['Metacritic Critic Score'] >= self.x))
        newlist = [] #create an appendable list with returned values
        newlist.append(metascores.dropna())#append in metascore without the NaN values
        newlist.append(users.dropna())#append in users without the NaN values
        return newlist.pop() #demonstration of the usage of linked list. This will return only the user rated album in the artists discography 
        


        
