def validate_move(move, board):
  is_valid_structure = validate_move_structure(move)

  if is_valid_structure:
    valid_move_array = valid_move_to_array(move)
    valid_placement = validate_move_placement(valid_move_array, board)

    return valid_placement


  # return valid_structure and valid_placement
  return False

def validate_move_structure(move):
  char = move[0]

  try:
    number = int(move[1]) - 1
  except (ValueError, IndexError):
    return False

  if ((char == "a" or char == "b" or char == "c") and (number == 0 or number == 1 or number == 2) ):
    return True
  else: 
    return False

def validate_move_placement(move, board):
  if board.board[move[0]][move[1]] == ' ': 
    return True
    
  return False

def valid_move_to_array(move):
  char, number = move[0], int(move[1]) - 1
  move_list = []
  converted_char = None

  if (char == "a"):
    converted_char = 0
  elif (char == "b"):
    converted_char = 1
  elif (char == "c"):
    converted_char = 2
  
  move_list.append(converted_char)
  move_list.append(number)

  return move_list

def check_winner(move, board, player):
  counter = 1
  max_dimension = len(board.board)

  for i in range(9):
    currentX = move[0]
    currentY = move[1]

    if (i == 0):
      xDiff = -1
      yDiff = -1
      while (currentX > 0 and currentX < max_dimension) and (currentY > 0 and currentY < max_dimension):
        currentX = currentX + xDiff
        currentY = currentY + yDiff
        mark = board.board[currentX][currentY]
        print('CurrentX: {0}, CurrentY: {1}. Mark is now {2}'.format(currentX, currentY, mark))
        if (mark == player):
          counter = counter + 1
    elif i == 1:
      print('Winner? {0}'.format(traverse(0, -1, move, board, player)))

  print('Counter is then {0}'.format(counter))

  if (counter == max_dimension):
    return True

  return False

def traverse(xDiff, yDiff, move, board, player):
  currentX = move[0]
  currentY = move[1]
  counter = 1
  max_dimension = len(board.board)

  while (currentX >= 0 and currentX < max_dimension) and (currentY >= 0 and currentY < max_dimension):
    currentX = currentX + xDiff
    currentY = currentY + yDiff
    mark = board.board[currentX][currentY]
    print('CurrentX: {0}, CurrentY: {1}. Mark is now \'{2}\''.format(currentX, currentY, mark))

    if mark == player:
      counter = counter + 1
    

  if counter == max_dimension:
    return True

  return False