class Board:
  def __init__(self, size = 3):
    self.board = [[' ']*size for i in range(size)]

  def print_board(self):
    print("     A   B   C")
    print("   -------------")
    print(" 1 | {0} | {1} | {2} |".format(self.board[0][0], self.board[1][0], self.board[2][0]))
    print("   -------------")
    print(" 2 | {0} | {1} | {2} |".format(self.board[0][1], self.board[1][1], self.board[2][1]))
    print("   -------------")
    print(" 3 | {0} | {1} | {2} |".format(self.board[0][2], self.board[1][2], self.board[2][2]))
    print("   -------------")

  def place_move(self, player, x, y):
    self.board[x][y] = player