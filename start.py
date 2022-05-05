import sys
import moves
print('Start')


ended = False
moveList = list()



while not(ended):
    
    turnMoves=list()
    
    for p in range(2):

        player_input = "invalid"
        while not(moves.is_valid_move(player_input)):
            print("player " + str(p) + ":")
            player_input = str.strip(sys.stdin.readline())
        turnMoves.append(player_input)
    moveList.append(turnMoves)
    if player_input == "X":
        ended = True

print(moveList)
        
