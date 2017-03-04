#!/usr/bin/env python

"""
Simple Sudoku solver
"""


class SudokuError(Exception):
    pass


class Sudoku(object):
    def __init__(self, sudoku_string):
        self.sudoku_string = sudoku_string
        self.check_string()
        self.board = self.create_board()

    def check_string(self):
        if len(self.sudoku_string) != 81:
            raise SudokuError("Incorrect board length")
        for c in self.sudoku_string:
            if not c.isdigit() and c != '.':
                raise SudokuError("Unrecognized character")

    def create_board(self):
        board = ()
        for c in self.sudoku_string:
            if c == '.':
                board += (tuple(range(1, 10)),)
            else:
                board += ((int(c),),)
        return board

    def solve(self):
        self.board = self.solver(self.board)

    @property
    def solved(self):
        return self.is_solved(self.board)

    def is_solved(self, board):
        for cell in board:
            if len(cell) != 1:
                return False
        return True

    def solver(self, board):
        modified = True
        while modified:
            modified = False
            for i, cell in enumerate(board):
                if len(cell) > 0:
                    invalid = self.invalid_numbers(i, board)
                    new_cell = tuple(
                        number for number in cell if number not in invalid
                    )
                    if new_cell != cell:
                        modified = True
                        new_board = list(board)
                        new_board[i] = new_cell
                        board = tuple(new_board)
                else:
                    raise SudokuError("Impossible to solve")
        if not self.is_solved(board):
            min_index = None
            min_cell = ()
            min_unknowns = 10
            for i, cell in enumerate(board):
                if 1 < len(cell) < min_unknowns:
                    min_index = i
                    min_cell = cell
                    min_unknowns = len(cell)
            for number in min_cell:
                new_board = list(board)
                new_board[min_index] = (number,)
                board = tuple(new_board)
                try:
                    return self.solver(board)
                except SudokuError:
                    pass
        else:
            return board
        raise SudokuError("Impossible to solve")

    def invalid_numbers(self, i, board):
        row = i / 9
        col = i % 9
        # Cells in the same row
        check = [j for j in xrange(row * 9, row * 9 + 9) if j != i]
        # Cells in the same column
        check += [j for j in xrange(col, 81, 9) if j != i]
        # Cells in the same square
        check += [
            9 * p + q for p in xrange(row / 3 * 3, row / 3 * 3 + 3)
            for q in xrange(col / 3 * 3, col / 3 * 3 + 3)
            if 9 * p + q != i and p != row and q != col
            ]
        # Return invalid values
        invalid = [
            cell[0] for i, cell in enumerate(board)
            if len(cell) == 1 and i in check
            ]
        return invalid

    def get_string(self, sep=''):
        if not self.solved:
            return "<Unsolved sudoku>"
        return sep.join([str(cell[0]) for cell in self.board])

    def __str__(self):
        string = ''
        for i, cell in enumerate(self.board):
            if i / 9 in [3, 6] and i % 9 in [0]:
                string += '------+-------+------\n'
            if len(cell) > 1:
                string += '?'
            else:
                string += str(cell[0])
            if i % 9 in [2, 5]:
                string += ' | '
            elif i % 9 in [8]:
                string += '\n'
            else:
                string += ' '
        return string


def convert_format(hts_sudoku):
    """Converts HTS format to conventional format
    """
    board = hts_sudoku.split(',')
    sudoku_string = ''
    for number in board:
        if not number:
            sudoku_string += '.'
        sudoku_string += number
    return sudoku_string


if __name__ == '__main__':
    sudoku_string = (
        '8........'
        '..36.....'
        '.7..9.2..'
        '.5...7...'
        '....457..'
        '...1...3.'
        '..1....68'
        '..85...1.'
        '.9....4..'
    )
    sudoku = Sudoku(sudoku_string)
    print sudoku
    sudoku.solve()
    print sudoku
    print sudoku.get_string(',')
