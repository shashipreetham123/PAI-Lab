import math
board = [".", ".", ".", ".", ".", ".", ".", ".", "."]

max_player = "X"
min_player = "O"

def game_status(board):
    combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],

        [0, 4, 8],
        [2, 4, 6],

        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8]
    ]
    result = None

    for combo in combinations :
        if board[combo[0]] == board[combo[1]] and board[combo[1]] == board[combo[2]] :
            result = board[combo[0]]
            break

    if result is None and "." not in board:
        result = "draw"

    return result  
    

def minimax(board, is_maximizing, depth):

    result = game_status(board)

    if result == max_player :
        return 10 - depth

    if result == min_player :
        return -10 + depth

    if result == "draw":
        return 0

    if (is_maximizing) :
        best_score = -math.inf

        for i in range(9) :
            if board[i] != "." : continue
            board[i] = max_player
            score = minimax(board, False, depth + 1)
            best_score = max(best_score, score)
            board[i] = "."

        return best_score
    else :
        best_score = math.inf

        for i in range(9) :
            if board[i] != "." : continue
            board[i] = min_player
            score = minimax(board, True, depth + 1)
            best_score = min(best_score, score)
            board[i] = "."

        return best_score


def find_best_move(board):
    move = -1
    best_score = -math.inf

    for i in range(9) :
        if board[i] != "." : continue
        board[i] = max_player
        score = minimax(board, False, 1)
        if score > best_score :
            best_score = score
            move = i
        board[i] = "."

    return move



    
def start_game() :

    for i in range(9) :
        board[i] = "."

    turn = input("Enter 1 to Play first (X) or 2 to Play second (O) : ")

    if turn == "1" :
        global max_player, min_player
        max_player = "O"
        min_player = "X"
        
        print_board(board.copy())

        while True :
            player_move = int(input("Enter your Move (0 - 8) : "))
            if player_move >= 0 and player_move <= 8 :
                board[player_move] = min_player
                break
            else :
                print("Invalid Move. Try Again")

    next_turn()
    

def next_turn():
    ai_move = find_best_move(board)
    board[ai_move] = max_player
    
    print_board(board.copy())

    result = game_status(board)

    if result == max_player :
        print ("You Lost")
        return
    if result == "draw" :
        print ("Draw")
        return


    while True :
        player_move = int(input("Enter your Move (0 - 8) : "))

        if player_move >= 0 and player_move <= 8 :
            if board[player_move] != ".":
                print ("Invalid Move! The Spot is already occupied")
            else :
                board[player_move] = min_player
                break   
        else :
            print("Invalid Move. Try Again")
         

    result = game_status(board)
    
    if result == min_player :
        print_board(board.copy())
        print ("You Win")
        return
    if result == "draw" :
        print_board(board.copy())
        print ("Draw")
        return

    next_turn()


def print_board(board) :

    n = 0

    for i in range(3) :
        for j in range(3) :
            print(board[n], end = " ")
            n = n + 1
        print()
    print()

start_game()

    

        
    

    
