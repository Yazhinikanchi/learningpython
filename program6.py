#FUNCTIONS lyk len,max,int,print,range...

num_char=len("hello")
print(num_char)

def my_function():
    print("hello")
    print("bye") #this code wont give any output cuz we didnt give fn yet

def my_function():
    print("hello")
    print("bye")

my_function() #first define the fn using def KEYWORD nd a name for it then a blank parenthesis ....put the lines of the code wiid indented...
#at last we should call the fn with parenthesis so that the codes will appear...



def turn_right():
      turn_left()
      turn_left()
      turn_left()
        
 #creating square

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_right()



#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
jump()
jump()
jump()
jump()
jump()
jump()
        


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(0,6):
    jump()



#

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    jump()




#HURDLE 3:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() == False:
    if wall_in_front():
        jump()
    else:
        move()
    
        
    
            
