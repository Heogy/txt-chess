import re
prog = re.compile("^((X|([NR][a-h]?x?|[NR][1-8]?x?|[a-hBQK]x)?[NBRQK]?[a-h][1-8]|([a-h]x)?[a-h][1-8][NBRQK]?|O-O|O-O-O)[\+#]?)$")

def is_valid_move(player_input):
    # print(player_input)
    return not(not(prog.match(player_input)))
