def read(fen):

    l = fen.split()
    state = dict()

    state['board'] = 'white'
    state['next'] = read_next(l[1])
    state['castles'] = read_castle(l[2])
    state['en_passant'] = read_en_passant(l[3])
    state['halfmove_clock'] = int(l[4])
    state['fullmove_number'] = int(l[5])
    return state

def read_en_passant(s):
    if s == '-':
        return ''
    else :
        return s

def read_castle(s):
    if s == '-':
        return list()
    else :
        return [char for char in s]

def read_next(next_char):
    if next_char == 'w':
        return 'white'
    elif next_char == 'b':
        return 'black'
    else :
        raise Exception()
