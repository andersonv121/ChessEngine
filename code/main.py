import chess
import chess.svg
import os

#os.chdir(os.path.dirname(os.path.abspath("/Volumes/Chess")))

board = chess.Board()

print(board)

print("")

move = chess.Move.from_uci("e2e4")
board.push(move)

print(board)

boardsvg = chess.svg.board(
    board,
  #  fill=dict.fromkeys(board.attacks(chess.E4), "#cc0000cc"),
 #   arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
  #  squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
    size=350,
)  

print("")

print(os.getcwd())

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
            print("Illegal move! Try again.\n")
    except:
        print("Sorry! Error.")




print(board)
print("\nGame over!")