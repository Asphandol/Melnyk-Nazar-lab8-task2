"""
Let's play a game!
"""
def validate_board(board:list) -> bool:
    """
    list(str) -> bool
    Chechs the values in game puzzle and says if it's played right or not.
    >>> validate_board(['**** ****', '***1 ****', '**  3****',\
'* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **',\
'  8  2***', '  2  ****'])
    False
    """
    total = len(board)
    for i in range(total):
        already_been = set()
        for m in range(total):
            if board[i][m] in already_been:
                return False
            else:
                if board[i][m].isdigit():
                    already_been.add(board[i][m])
    for k in range(total):
        already_been = set()
        for n in range(total):
            if board[n][k] in already_been:
                return False
            else:
                if board[n][k].isdigit():
                    already_been.add(board[n][k])
    for i in range(9):
        if board[0][i] != '*':
            width = 8 - i
            break
    for i in range(9):
        if board[i][8-i] != '*':
            diag = 8 - i
            break
    for j in range(diag):
        repeat = set()
        if board[8-j][j].isdigit():
            repeat.add(board[8-j][j])
        for b in range(1, width+1):
            if board[8-j-b][j] in repeat or board[8-j][j+b] in repeat:
                return False
            else:
                if board[8-j-b][j].isdigit():
                    repeat.add(board[8-j-b][j])
                if board[8-j][j+b].isdigit():
                    repeat.add(board[8-j][j+b])
    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
