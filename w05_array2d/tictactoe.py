win = False
b = [[' ']*3]*3


def pretty(a):
    for b in len(a):
        print(a[b].toString)

#the start() function has no parameters and will run at the
#beginning of the game to initialize which symbol a player has
def start():
    choose = input("Player 1, do you want to be X or O? \n")
    if (choose == 'X' or choose == 'x'):
        p1 = 'X'
        p2 = 'O'
        print('Player 1 is X, Player 2 is O')
    elif (choose == 'O' or choose == 'o'):
        p1 = 'O'
        p2 = 'X'
        print('Player 1 is O, Player 2 is X')
    else:
        start()
        
def move(p1, p2):
    pretty(b)
    #if (win == False):
        
    
start()
move('X', 'O')
    