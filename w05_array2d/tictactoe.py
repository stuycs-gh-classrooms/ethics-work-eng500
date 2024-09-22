win = False
b = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
sample = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
p1 = "X"
p2 = "O"


def arrprint(b):
    result = ''
    for i in range(len(b)):
        result += '['
        for n in range(len(b[i])):
            result += str(b[i][n])
            if n != 2:
                result += ' | '
        result += ']'
        if i != 2:
            result += '\n'
    print(result + '\n')

#the start() function has no parameters and will run at the
#beginning of the game to initialize which symbol a player has
def run():
    win = False
    print("Player 1 is X and Player 2 is O")
    print("This is a key for the different squares of the board:")
    arrprint(sample)
    while win == False:
        move(p1)
        win(p1)
        move(p2)
        win(p2)
    
def move(p):
    print('This is your current board: ')
    arrprint(b)
    if p == p1:
        pos = input ("Player 1: Which square would you like to move? Please use lowercase letters \n")
    else:
        pos = input ("Player 2: Which square would you like to move? Please use lowercase letters \n")
    if pos == 'a':
        if b[0][0] == ' ':
            b[0][0] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'b':
        if b[0][1] == ' ':
            b[0][1] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'c':
        if b[0][2] == ' ':
            b[0][2] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'd':
        if b[1][0] == ' ':
            b[1][0] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'e':
        if b[1][1] == ' ':
            b[1][1] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'f':
        if b[1][2] == ' ':
            b[1][2] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'g':
        if b[2][0] == ' ':
            b[2][0] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'h':
        if b[2][1] == ' ':
            b[2][1] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
    elif pos == 'i':
        if b[2][2] == ' ':
            b[2][2] = p
        else:
           print("This square is taken up. Choose a different one.")
           move(p)
def win(p):
    if b[0][0] == p and b[0][1] == p and b[0][2] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[1][0] == p and b[1][1] == p and b[1][2] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[2][0] == p and b[2][1] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[0][0] == p and b[1][0] == p and b[2][0] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[0][1] == p and b[1][1] == p and b[2][1] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[0][2] == p and b[1][2] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[0][0] == p and b[1][1] == p and b[2][2] == p:
        win = True
        print(f"Yay {p} won!")
    elif b[2][0] == p and b[1][1] == p and b[0][2] == p:
        win = True
        print(f"Yay {p} won!")
            
run()

    