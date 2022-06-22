#Matthew Rothman weight and height guessing Game
#To create a program that provides certain outputs based on what the user guesses
#for the height and weight


# Defined the inputs I want here 
weight = int(input("Enter weight here: "))
height = int(input("Enter height in inches here: "))

#This line checks for the first condition to see if it return "Both Higher"
if weight > 180 and height > 67:
    print("both higher: ")

#This line checks for the condition of both lower

if weight < 180 and height < 67:
    print("both lower: ")

#If the user enters the right number they will get bingo

if weight == 180 and height == 67:
    print("bingo: ")

#The next two lines are to check the condititon of one number
#bbeing higher and one number being lower

if weight > 180 and height < 67:
    print("Game over: ")

if weight < 180 and height > 67:
    print("Game over: ")

#I tested what would happen if they guess one number right
#and one wrong and it caused a bug
#Therefore I created the next four lines to to fix this bug
#If someones guesses one right number but one wrong then the
#the system will return game over
    
if weight == 180 and height > 67:
    print("Game over: ")

if weight == 180 and height < 67:
    print("Game over: ")

if weight > 180 and height == 67:
    print("Game over: ")

if weight < 180 and height == 67:
    print("Game over: ")


