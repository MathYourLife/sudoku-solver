# sudoku-solver

A fun into to py project of training a python script to solve sudoku puzzles without guessing.  You can add logic onto it own your own.  If you get stuck, take a look at some more advanced techniques [here](https://www.sudokuoftheday.com/techniques/) that you could add.

## sudoku-solver.py

The sudoku-solver.py script as-is:

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

## Running Out of the Box

`python sudoku-solver.py`

```
Loading a sudoku board...
Starting board configuration
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

Since a 3 is located at (1, 2) remove the number 3 as an option
from all cells in row 1 and column 2
note: row and column designations are zero-based
Show the remaining cells that are allowed to have the number 3
-------------
|X3 |33X|333|
|XX3|   | XX|
|X3X|333|XX3|
-------------
|33X|333|33X|
|33 |X3X|333|
|X3 |X33|X33|
-------------
|3XX|333|X3X|
|X3 |333|XXX|
|33 |XX3|33X|
-------------

Cells that are known (i.e. have only one option) are marked with an X
```


Enjoy!
