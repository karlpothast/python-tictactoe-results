import create_board as cb


def check_winner(board):
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
    

def process_results():
  board = cb.create_board()
  winner = check_winner(board)
  if (winner == None):
    winner = "Draw"
    print('winner: ' + winner + "\n") 
  else:
    print('winner: ' + winner + "s\n") 


  for row in board:
      print(row)


def main():
  process_results()


if __name__ == '__main__':
    main()