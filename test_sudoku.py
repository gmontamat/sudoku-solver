#!/usr/bin/env python

"""
Unit test cases for the Sudoku class
"""

import sudoku
import timeit
import unittest

# Some unsolved sudokus
SUDOKU_HTS1 = (
    '9,3,6,,,8,7,1,4,1,4,7,6,,,,2,5,,,,7,4,,,,6,6'
    ',9,3,,,5,4,7,1,,,,,9,,5,8,,8,,5,,1,7,6,,3,,,'
    ',1,,4,3,6,9,4,7,1,9,6,3,2,5,8,,,9,,,2,1,4,7'
)
SUDOKU_HTS2 = (
    ',2,5,7,1,4,6,,9,9,,,,2,,,4,1,,4,7,9,3,6,8,,2,'
    '5,8,,,,1,3,,6,6,9,3,,8,2,4,1,7,7,,,6,,,5,2,8,'
    '4,,1,3,,,,8,5,3,,9,,5,,,7,,,5,8,1,,7,9,,3'
)
SUDOKU_EASY = (
    '8..6..9.5.............2.31.'
    '..7318.6.24.....73.........'
    '..279.1..5...8..36..3......'
)
SUDOKU_MEDIUM = (
    '6.7.9.5.4....4....9..7.6..2'
    '..5...2..38.....46..9...8..'
    '5..4.2..9....1....7.6.3.4.5'
)
SUDOKU_HARD = (
    '8..........36......7..9.2..'
    '.5...7.......457.....1...3.'
    '..1....68..85...1..9....4..'
)


class TestSudoku(unittest.TestCase):
    def test_convert_format(self):
        self.assertEqual(
            sudoku.convert_format(SUDOKU_HTS1),
            '936..87141476...25...74...6693..5471....9'
            '.58.8.5.176.3...1.4369471963258..9..2147'
        )
        self.assertEqual(
            sudoku.convert_format(SUDOKU_HTS2),
            '.257146.99...2..41.479368.258...13.6693.8'
            '24177..6..5284.13...853.9.5..7..581.79.3'
        )

    def test_Sudoku_is_solved(self):
        s = sudoku.Sudoku(
            '82571463993682574114793685258247139669358'
            '2417714693528471369285369258174258147963'
        )
        self.assertTrue(s.solved)
        s = sudoku.Sudoku(
            '93625871414763982525874193669382547171439'
            '6582825417693582174369471963258369582147'
        )
        self.assertTrue(s.solved)

    def test_Sudoku_solve(self):
        string = sudoku.convert_format(SUDOKU_HTS1)
        s = sudoku.Sudoku(string)
        s.solve()
        self.assertTrue(s.solved)
        string = sudoku.convert_format(SUDOKU_HTS2)
        s = sudoku.Sudoku(string)
        s.solve()
        self.assertTrue(s.solved)


def time_solver(sudoku_string):
    t = timeit.default_timer()
    s = sudoku.Sudoku(sudoku_string)
    s.solve()
    return timeit.default_timer() - t


if __name__ == '__main__':
    print "Speed test"
    print "----------"
    print "Easy runtime: {}".format(time_solver(SUDOKU_EASY))
    print "Medium runtime: {}".format(time_solver(SUDOKU_MEDIUM))
    print "Hard runtime: {}".format(time_solver(SUDOKU_HARD))
    print
    unittest.main()
