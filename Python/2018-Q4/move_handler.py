def validate_move(move, board):
  valid_structure = validate_move_structure(move)
  valid_placement = validate_move_placement(move, board)

  return valid_structure and valid_placement

def validate_move_structure(move):
  char = move[0]

  try:
    number = int(move[1]) - 1
  except ValueError: 
    return False

  if ((char == "a" or char == "b" or char == "c") and (number == 0 or number == 1 or number == 2) ):
    return True
  else: 
    return False

def validate_move_placement(move, board):
  return True

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