import os 
from random import randrange

#Action :  reload  deflect defend fire 
#Resule : win, lose, lost2, tie  
#Rule: 
#       you can only fire when you have at least one bullet in magazine 
#       you can only deflect when you have at least five bullet in magazine  
#       if play one has fault action, the penlty is play two's action is fire, then, play one lose 
#       there are 0 bullets in the magazine initiallly

# use reload count 
win_x = 0
win_y = 0
lose_x = 0 
lose_y = 0 
mag_x = 0 
mag_y = 0 
name_x = "Computer"
name_y = "Human"

def play ( x, y) :
    global win_x, win_y, lose_x, lose_y, mag_x, mag_y, name_x, name_y
    result = judge(x, y)

    if x == "reload" :
        mag_x = mag_x + 1
    if y == "reload" :
        mag_y = mag_y + 1 
    if x == "fire" and mag_x > 0:
        mag_x = mag_x - 1
    if y == "fire" and mag_y > 0:
        mag_y = mag_y - 1 

    if result == "win":
        win_x = win_x + 1 
        lose_y = lose_y + 1
    elif result == "lose":
        lose_x = lose_x + 1 
        win_y = win_y + 1 
    elif result == "lose2":
        lost_x = lose_x + 1 
        lose_y = lose_y + 1
    return result

def judge  ( x , y) :
    global win_x, win_y, lose_x, lose_y, mag_x, mag_y, name_x, name_y

    fault_x = False
    fault_y = False

    if ( x == "fire" and mag_x == 0 ) or ( x == "deflect" and mag_x < 5) :
        fault_x = True 
    if ( y == "fire" and mag_y == 0 ) or ( y == "deflect" and mag_y < 5) :
        fault_y = True 
    
    if fault_x :
        if fault_y : 
            return "tie"  
        else: 
            if y == "fire":
                return "lose"
            elif y == "reload" or y == "deflect" or y == "defend":
                return "tie"
    else:
        if x ==  "reload":
            if fault_y or y == "reload" or y == "deflect" or y == "defend" :
                return "tie"
            elif y == "fire" :
                return "lose"
        elif x == "deflect" :
            if fault_y or y == "reload" or y == "deflect" or y ==  "defend" :
                return "tie"
            elif y == "fire":
                return "win"
        elif x == "defend":
            if fault_y or y == "reload" or y == "deflect" or y ==  "defend" or y == "fire" :
                return "tie"
        elif x == "fire":
            if fault_y : 
                return "win"
            elif y == "reload" :
                return "win"
            elif y == "deflect" :
                return "lose"
            elif y == "defend" :
                return "tie"
            elif y == "fire" :
                return "lose2"

def printAction (x, y ) :
    global win_x, win_y, lose_x, lose_y, mag_x, mag_y, name_x, name_y
    print ("\t\t{}                               {}".format(  x,  y ) )
    print ("\t\t{}                                    {}".format(  mag_x,  mag_y ) )

def printResult( result ) :
    global win_x, win_y, lose_x, lose_y, mag_x, mag_y, name_x, name_y

    print ("\t\t{}             {}             {}".format(name_x, result.upper(), name_y))
    print ("\t\tW - L - B                            W - L - B")
    print ("\t\t{}-{}-{}                               {}-{}-{}".format(win_x, lose_x, mag_x, win_y, lose_y, mag_y) )
    
def gen_act ( ) :
    act = randrange( 1, 5) 
    if act == 1 :
        return "reload"
    elif act == 2 :
        return "deflect" 
    elif act == 3 :
        return "defend"
    elif act == 4 :
        return "fire"
def get_act () :
    act = "" 
    while act not in ["reload", "deflect", "defend", "fire"] :
        act = input('Enter your action: ["reload", "deflect", "defend", "fire"]')
    return act



def unit_test( ) :
    x = "reload"
    y = "reload" 
    play ( x, y)
    play ( x, y)
    y = "fire"
    printResult ( play ( x, y ))
# unit_test ()
for i in range(100) :
    print ("\t\t---------------Playing round:{}--------------".format(i) ) 
    x = get_act()
    y = gen_act() 

    printAction(x, y)
    printResult( play(x, y)) 

print ("\t\t---------------finished--------------" ) 
