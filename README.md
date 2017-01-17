# sudoku-solver

Sudoku solver implemented in Python 2.7

## Note

The solver works very well on any 9x9 puzzle but the main purpose of this repo is to improve the style of the original code and make it more readable.

## World's hardest Sudoku

```python
import sudoku

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
hard_sudoku = sudoku.Sudoku(sudoku_string)
hard_sudoku.solve()
print hard_sudoku
```

```
8 1 2 | 7 5 3 | 6 4 9
9 4 3 | 6 8 2 | 1 7 5
6 7 5 | 4 9 1 | 2 8 3
------+-------+------
1 5 4 | 2 3 7 | 8 9 6
3 6 9 | 8 4 5 | 7 2 1
2 8 7 | 1 6 9 | 5 3 4
------+-------+------
5 2 1 | 9 7 4 | 3 6 8
4 3 8 | 5 2 6 | 9 1 7
7 9 6 | 3 1 8 | 4 5 2
```

## Unit testing

```
python2 test_sudoku.py
```

```
Speed test
----------
Easy runtime: 0.286250829697
Medium runtime: 0.0661108493805
Hard runtime: 9.63975000381

...
----------------------------------------------------------------------
Ran 3 tests in 0.035s

OK
```
