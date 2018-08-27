from board import Board
import move_handler

board = Board()

p1, p2 = "x", "o"
p1_turn = True
game_over = False

board.print_board()
print("Welcome to tic-tac-toe! Player 1 begins: ")

while(not game_over):
  current_player = p1 if p1_turn else p2
  player_name = "Player 1" if p1_turn else "Player 2"
  is_valid_move = False
  move = None

  while (not is_valid_move):
    move = input("Where does {0} place an '{1}'? ".format(player_name, current_player))
    is_valid_move = move_handler.validate_move(move, board)
    print("Is move valid?", is_valid_move)
  
  valid_move = move_handler.valid_move_to_array(move)

  board.place_move(current_player, valid_move[0], valid_move[1])
  board.print_board()
  print("---------------------------------")

  # Do stuff
  p1_turn = not p1_turn