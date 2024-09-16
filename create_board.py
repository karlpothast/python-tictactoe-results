import random

def check_winner(board):
    global winner
    for row in board:                                                           # check 3 in a row horizontally
      if (row[0] != "") and (row[0] == row[1] == row[2] and row[0]):
        return row[0]
    for col in range(3):                                                        # check 3 in a row vertically
      if (board[0][col] != "") and (board[0][col] == board[1][col] == board[2][col]):
        return board[0][col]
    if (board[0][0] != "") and (board[0][0] == board[1][1] == board[2][2]):     # check 3 in a row diagonally 1
      return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]):                             # check 3 in a row diagonally 2
      return board[0][2]

def create_board():
  board = [[" " for _ in range(3)] for _ in range(3)]
  position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  simulate_game(board, position_list, 1)
  return board

def simulate_game(board, position_list, move_num):
  # X traditionally starts the game so move 1 & all subsequent moves by X will be odd ad all evens will be Os
  player = "O" if move_num % 2 == 0 else "X"
  random_grid_position = random.choice(position_list)  # get random position on grid - numbers 1 through 9 represent the squarea in tic tac toe
  match random_grid_position:
    case 1:
      board[0][0] = player 
    case 2:
      board[0][1] = player 
    case 3:
      board[0][2] = player 
    case 4:
      board[1][0] = player 
    case 5:
      board[1][1] = player 
    case 6:
      board[1][2] = player
    case 7:
      board[2][0] = player
    case 8:
      board[2][1] = player
    case 9:
      board[2][2] = player
  position_list.remove(random_grid_position)
  if (len(position_list) > 0):
  #check if game has been won before recursing to end
    winner = check_winner(board)
    if (winner == "X") or (winner == "O"):
      return board
    simulate_game(board, position_list, move_num+1)
  