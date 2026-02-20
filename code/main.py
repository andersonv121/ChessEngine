gimport chess
import random
import time


depth = 2


positions_evaluated = 0


# assigns values to each piece -- used for evaluating board positions
piece_values = {
   chess.PAWN: 1,
   chess.KNIGHT: 3,
   chess.BISHOP: 3,
   chess.ROOK: 5,
   chess.QUEEN: 9,
}


# initialize the board
board = chess.Board()




# creates a material-based score:
# positive favors Black, negative favors White
def evaluate(board):


   if board.is_checkmate():
       return -9999 if board.turn == chess.BLACK else 9999
  
   score = 0
  
   for piece_type in piece_values:
       score += len(board.pieces(piece_type, board.turn)) * piece_values[piece_type]
       score -= len(board.pieces(piece_type, not board.turn)) * piece_values[piece_type]




   return score




# recursive function that evaluates positions until the depth limit is reached
def minimax(board, depth):
   if depth == 0 or board.is_game_over():
       return evaluate(board)
  
   best_score = -9999


   for move in board.legal_moves:
       board.push(move)
       score = -minimax(board, depth - 1)
       board.pop()


       best_score = max(best_score, score)


   return best_score


# chooses the best move by searching future positions
def get_best_move(board):
   positions_evaluated = 0


   best_moves = []
   best_score = -9999


   start_time = time.time()


   for move in board.legal_moves:
       board.push(move)
       score = minimax(board, depth - 1)
       board.pop()


       if score > best_score:
           best_score = score
           best_moves = [move]
       elif score == best_score:
           best_moves.append(move)


   elapsed = time.time() - start_time


   return random.choice(best_moves), positions_evaluated, elapsed




# main game loop
while not board.is_game_over():
   print(board)
   print()


   if board.turn == chess.WHITE:
       move_input = input("White move: ").strip()


       if move_input == "1":
           print("White resigns!")
           break


   else:
       move, positions_considered = get_best_move(board)
       move_input = move.uci()


       print(f"Positions considered: {positions}")
       print(f"Black move: {elapsed} seconds")


   try:
       move = chess.Move.from_uci(move_input)


       if move in board.legal_moves:
           board.push(move)
       else:
           print("Illegal move!\n")


   except Exception:
       print("Sorry! Error.")




print(board)
print("\nGame over!")



