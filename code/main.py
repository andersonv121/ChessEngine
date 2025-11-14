import chess
import os

board = chess.Board()

while not board.is_game_over():
    print(board)
    print("")

    color = "White" if board.turn == chess.WHITE else "Black"
    move_input = input(f"{color} move: ").strip()

    try:
        move = chess.Move.from_uci(move_input)
        if move in board.legal_moves:
            board.push(move)
        else:
            print("Illegal move!\n")
    except:
        print("Error.")

print(board)
print("\nGame over!")
print(board)
print("\nGame over!")
