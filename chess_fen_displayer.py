
# unicode codes start from 9812 (white king) to 9823 (black pawn) [2654, 265f] hex
symbols = {'P':'♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
           'p':'♟︎', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'}

whitesAndBlacks = [('□', '■'), ('░', '▓'), ('░', '█'), ('▏▔', '█')]

def convert_fen_to_board(fen, differEmptyCells=True, emptyCell='.',
                         whiteAndBlack=whitesAndBlacks[2]):
    result = ''

    w, b = whiteAndBlack

    lines = fen.split('/')
    for i in range(len(lines)):
        #emptyCells = [(b+w, w+b)[i%2==0] for _ in range(4)]
        emptyCells = [((w,b)[j%2==0], (b,w)[j%2==0])[i%2==0] for j in range(8)]
        line = ''
        colInd = 0 #here we use this because the pawn is two characters
        for j in lines[i]:
            if(j.isdigit()):
                if differEmptyCells:
                    line += ''.join(emptyCells[colInd: colInd + int(j)])
                else:
                    line += emptyCell*int(j)
                colInd += int(j)
            else:
                line += symbols[j]
                colInd += 1
        result += line + '\n'

    print(result)
