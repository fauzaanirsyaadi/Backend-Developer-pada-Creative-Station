class Sudoku:
    def __init__(self):
        self.board = None
        self.fixed_coords = set()

    def load_board(self, filename):
        # load board from file
        self.board = []
        with open(filename, 'r') as f:
            for line in f:
                row = [int(num) for num in line.split()]
                self.board.append(row)

        # find fixed coordinates
        self.fixed_coords = set()
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.fixed_coords.add((i, j))

    def add_number(self, row, col, num):
        # check if coordinate is fixed
        if (row, col) in self.fixed_coords:
            print("Error: This coordinate is fixed!")
            return

        # check if number is valid
        if not self.is_valid(row, col, num):
            print("Error: Invalid number!")
            return

        # add number to board
        self.board[row][col] = num

    def is_valid(self, row, col, num):
        # check row and column
        for i in range(9):
            if self.board[row][i] == num:
                return False
            if self.board[i][col] == num:
                return False

        # check subgrid
        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, subgrid_row+3):
            for j in range(subgrid_col, subgrid_col+3):
                if self.board[i][j] == num:
                    return False

        return True

    def clear_board(self):
        # reset board to last loaded file
        if self.board is not None:
            self.load_board(self.last_loaded_file)

    def draw_board(self):
        # draw board in cmd line
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=' ')
                if j % 3 == 2:
                    print('|', end=' ')
            print()
            if i % 3 == 2:
                print('-' * 21)

if __name__ == '__main__':
    sudoku = Sudoku()
    while True:
        command = input("Enter command (L, A, R, C, Q): ")
        if command == 'L':
            filename = input("Enter filename: ")
            sudoku.load_board(filename)
            sudoku.last_loaded_file = filename
            sudoku.draw_board()
        elif command == 'A':
            row, col, num = input("Enter coordinates (row,col,num): ").split(',')
            row, col, num = int(row)-1, int(col)-1, int(num)
            sudoku.add_number(row, col, num)
            sudoku.draw_board()
        elif command == 'R':
            sudoku.draw_board()
        elif command == 'C':
            sudoku.clear_board()
            sudoku.draw_board()
        elif command == 'Q':
            break

# how to run ?
# python sudoku.py