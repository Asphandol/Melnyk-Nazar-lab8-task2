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
    return True

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
