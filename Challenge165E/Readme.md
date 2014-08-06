# Description

This first challenge is based on a game (the mathematical variety - not quite 
as fun!) called Conway's Game of Life. This is called a cellular automaton. 
This means it is based on a 'playing field' of sorts, made up of lots of 
little cells or spaces. For Conway's game of life, the grid is square - but 
other shapes like hexagonal ones could potentially exist too. Each cell can 
have a value - in this case, on or off - and for each 'iteration' or loop of 
the game, the value of each cell will change depending on the other cells 
around it. This might sound confusing at first, but looks easier when you 
break it down a bit.
A cell's "neighbours" are the 8 cells around it.
If a cell is 'off' but exactly 3 of its neighbours are on, that cell will also 
turn on - like reproduction.
If a cell is 'on' but less than two of its neighbours are on, it will die out -
 like underpopulation.
If a cell is 'on' but more than three of its neighbours are on, it will die 
out - like overcrowding.
Fairly simple, right? This might sound boring, but it can generate fairly 
complex patterns - this one, for example, is called the Gosper Glider Gun and 
is designed in such a way that it generates little patterns that fly away from 
it. There are other examples of such patterns, like ones which grow 
indefinitely.
Your challenge is, given an initial 'state' of 'on' and 'off' cells, and a 
number, simulate that many steps of the Game of Life.

# Formal Inputs and Outputs

## Input Description
You will be given a number N, and then two more numbers X and Y. After that 
you will be given a textual ASCII grid of 'on' and 'off' states that is X 
cells wide and Y cells tall. On the grid, a period or full-stop . will 
represent 'off', and a hash sign # will represent 'on'.
The grid that you are using must 'wrap around'. That means, if something goes 
off the bottom of the playing field, then it will wrap around to the top, like 
this: http://upload.wikimedia.org/wikipedia/en/d/d1/Long_gun.gif See how those 
cells act like the top and bottom, and the left and right of the field are 
joined up? In other words, the neighbours of a cell can look like this - where 
the lines coming out are the neighbours:

    #-...-  ......  ../|\.
    |\.../  ......  ......
    ......  |/...\  ......
    ......  #-...-  ......
    ......  |\.../  ..\|/.
    |/...\  ......  ..-#-.

## Output Description
Using that starting state, simulate N iterations of Conway's Game of Life. 
Print the final state in the same format as above - . is off and # is on.