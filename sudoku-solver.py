"""
Solving a Sudoku without Guessing in Python

Author: Dan Couture (MathYourLife)

This is meant to provide a starting structure for someone to extend into
a sudoku solver.

As-is it:

* Has a class called Board
* Starts out with all 81 cells capable of any number 1-9
* Can load a starting board for testing
* Can print out a "pretty" view of the known cell values
* Can set the value of a cell to a known number
* Can remove a number as an option for a cell
* Can show any remaining options for a certain number

* Has 2 starter solution techniques
  * remove a number as an option from a row
  * remove a number as an option from a column

"""

class Board(object):
    def __init__(self, board_str):
        """
        This is the method that gets called when the Board() object
        is created.
        """
        self.board = []
        self.create_board()
        self.load_starting_board(board_str)

    def create_board(self):
        """
        Initialize the board with a 9x9 with each cell having the
        options 1-9 available.
        """

        # Add 9 rows to the board
        for row in range(9):
            self.board.append([])

            # For each row, add 9 cells
            for col in range(9):
                self.board[row].append(list(range(1,10)))

    def load_starting_board(self, board_str):
        """
        Convenience method that takes the string representation of the
        board and loads it.
        """

        # Remove all formatting characters so you have an 81 character string
        board_str = board_str.replace('-', '')
        board_str = board_str.replace('|', '')
        board_str = board_str.replace('\r', '')
        board_str = board_str.replace('\n', '')

        # Loop through the cells and set the value if it's not blank
        row = 0
        col = 0
        for value in board_str:
            if value != " ":
                self.set_cell(row, col, int(value))
            # Move to the next column
            col += 1
            # If we're at the end of the row, go to the next
            if col == 9:
                col = 0
                row += 1

    def __str__(self):
        """
        Creates a string representation of the board for printing
        """

        board_str = "-" * 13 + "\r\n"
        for row in range(9):
            row_str = "|"
            for col in range(9):
                if len(self.board[row][col]) == 1:
                    # if there is only one option left the cell is "known"
                    row_str += str(self.board[row][col][0])
                else:
                    # more than 1 option = unknown
                    row_str += " "
                # end of a 3x3, add a vertical line
                if col % 3 == 2:
                    row_str += "|"
            board_str += row_str + "\r\n"
            if row % 3 == 2:
                board_str += "-" * 13 + "\r\n"
        return board_str

    def set_cell(self, row, col, value):
        self.board[row][col] = [value]

    def remove_option(self, row, col, value):
        if len(self.board[row][col]) == 1:
            return
        try:
            self.board[row][col].remove(value)
        except ValueError:
            # This error gets thrown if the value has already
            # been removed from this cell.
            pass

    def show_locations(self, value):
        """
        Very similar to the __str__ method that shows the current board
        In this case print:
            * X if the cell is known to be another number
            * empty if the cell can't be the number
            * the number if still a possibility or known to be it
        """
        board_str = "-" * 13 + "\r\n"
        for row in range(9):
            row_str = "|"
            for col in range(9):
                if value in self.board[row][col]:
                    # cell can be or is the value
                    row_str += str(value)
                elif len(self.board[row][col]) == 1:
                    # cell in known to be another number
                    row_str += "X"
                else:
                    # Cell is unknown
                    row_str += " "
                # Add a vertical line at the end of a 3x3
                if col % 3 == 2:
                    row_str += "|"
            board_str += row_str + "\r\n"
            if row % 3 == 2:
                board_str += "-" * 13 + "\r\n"
        return board_str


################################################################
# Search and Destroy Methods
# Here's where you can create smaller sections of logic
# that do things like remove all the 3's as an option from row 2

def clear_row(b, row, value):
    """ Remove 'value' as an option from 'row' """
    for col in range(9):
        b.remove_option(row, col, value)

def clear_col(b, col, value):
    """ Remove 'value' as an option from 'col' """
    for row in range(9):
        b.remove_option(row, col, value)


################################################################
# The central solving routine

def solve(board_str):
    """
    SOLVE IT!
    """

    print("Loading a sudoku board...")
    b = Board(board_str)
    print("Starting board configuration")
    print(b)

    print("Since a 3 is located at (1, 2) remove the number 3 as an option")
    print("from all cells in row 1 and column 2")
    print("note: row and column designations are zero-based")

    clear_row(b, 1, 3)
    clear_col(b, 2, 3)

    print("Show the remaining cells that are allowed to have the number 3")
    print(b.show_locations(3))
    print("Cells that are known (i.e. have only one option) are marked with an X")


################################################################
# Sample Boards

easy_1 = """
-------------
|9  | 34|   |
|723|   | 48|
|1 4|   |79 |
-------------
|  6|  3|  1|
|   |8 2|   |
|2  |9  |8  |
-------------
| 71|   |4 6|
|63 |   |915|
|   |15 |  7|
-------------
"""

if __name__ == "__main__":
    """ This is the script starting location """

    # We're going to work on the easy_1 board
    solve(easy_1)
