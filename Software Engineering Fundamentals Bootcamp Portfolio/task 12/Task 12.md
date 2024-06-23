Task 12 uses 2D lists to create data structures

This task involves creating a minesweeper board made up of [-] and [#]
First a grid is created, then show_template prints the grid
Then number_grid uses a for loop to append the grid using numbers to indicated mine locations
During this loop we get one item from the list at a time then check all directions to see if we find a mine
When we find a mine we then a place a number to represent how many mines are nearby the element
we then move onto the the next index and repeat the process
There is handling to make sure we do not check for mines outside the game board as this would ruin the printout
