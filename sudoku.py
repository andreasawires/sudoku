import numpy as np

def empty(grid):
    # check if there is any place empty i.e. equals to 0
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)

    return None

def possible(grid, row, col, n):

    # get the position of the box
    box_x = (col//3)*3
    box_y = (row//3)*3

    # iterate over row and columns
    for i in range(9):
        if grid[row][i] == n or grid[i][col] == n:
            return False

    # itererate over the box
    for i in range(3):
        for j in range(3):
            if grid[box_y+i][box_x+j] == n:
                return False

    return True

def solve(grid):
    position = empty(grid)

    if not position:
        return True
    else:
        row, col = position

    for n in range(1, 10):
        if possible(grid, row, col, n):
            grid[row][col] = n

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

if __name__ == "__main__":

    grid = [[7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]]

    solve(grid)

    print(np.matrix(grid))