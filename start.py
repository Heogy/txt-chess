import sys
import re

print('Start')


ended = False
moveList = list()

prog = re.compile("^(X|([NR][a-h]?x?|[NR][1-8]?x?|[a-hBQK]x)?[NBRQK]?[a-h][1-8]|([a-h]x)?[a-h][1-8][NBRQK]?|O-O|O-O-O)$")

def is_valid_move(player_input):
    # print(player_input)
    return not(not(prog.match(player_input)))


while not(ended):
    
    turnMoves=list()
    
    for p in range(2):

        player_input = "invalid"
        while not(is_valid_move(player_input)):
            print("player " + str(p) + ":")
            player_input = str.strip(sys.stdin.readline())
        turnMoves.append(player_input)
    moveList.append(turnMoves)
    if player_input == "X":
        ended = True

print(moveList)
        
