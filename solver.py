# solver.py
examplePuzz = [
            [0, 0, 4, 0, 9, 8, 3, 7, 5],
            [5, 7, 0, 0, 0, 6, 2, 9, 1],
            [0, 9, 2, 1, 0, 7, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 5, 6, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 1, 6, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 6, 0, 2, 8, 5, 0],
            [0, 4, 0, 3, 0, 0, 0, 2, 6],
            [6, 2, 9, 5, 8, 0, 4, 0, 0]]

def filled(puzzle):
    '''Determines if the puzzle is entirely filled.'''
    for row in puzzle:
        if 0 in row: return False
    return True

def firstUnused(puzzle):
    '''Returns the [row, col] of the topmost-leftmost 0 in puzzle'''
    for i, row in enumerate(puzzle):
        if 0 in row:
            zeroAt = row.index(0)
            return [i, zeroAt]

def checkSquare(num, row, col, puzzle):
    '''Determines if num is valid at puzzle[row][col] based on
    the 3x3 box it resides in
    '''
    yPos = row % 3
    xPos = col % 3

    if yPos == 0:
        yRange = range(row, row+3)
    elif yPos == 1:
        yRange = range(row-1, row+2)
    elif yPos == 2:
        yRange = range(row-2, row+1)

    if xPos == 0:
        xRange = range(col, col+3)
    elif xPos == 1:
        xRange = range(col-1, col+2)
    elif xPos == 2:
        xRange = range(col-2, col+1)

    for i in yRange:
        for j in xRange:
            if puzzle[i][j] == num:
                return False
    return True

def addNum(puzzle):
    '''Returns a list of puzzles with the firstUnused(puzzle) replaced with
    1 <= i <= 9, if i is valid in that position
    '''
    unused = firstUnused(puzzle)
    row = unused[0]
    col = unused[1]
    puzzRow = puzzle[row]
    puzzLen = len(puzzle)
    res = []
    for i in range(1, 10):
        valid = True
        for j in range(puzzLen):
            if puzzRow[j] == i or puzzle[j][col] == i:
                valid = False
                continue
        if not valid: continue
        valid = checkSquare(i, row, col, puzzle)
        if not valid: continue
        r = [puzzle[j][:] for j in range(len(puzzle))]
        r[row][col] = i
        res.append(r)
    return res

def solveFromList(puzzles):
    '''Produces the solution for one of the puzzles or False'''
    if puzzles == []:
        return False
    else:
        cur = solve(puzzles[0])
        if not cur:
            if puzzles == []:
                return False
            else: return solveFromList(puzzles[1:])
        return cur

def solve(puzzle):
    '''Produces the solved puzzle or False'''
    if filled(puzzle):
        return puzzle
    else: return solveFromList(addNum(puzzle))

def main():
    print("Use this tool to solve sudoku.")
    print("Enter each line of the puzzle one at a time,")
    print("Using 0 to denote empty squares.")
    print("Any characters after the first 9 on each line will be ignored.")
    puzzle = []
    for i in range(9):
        puzzle.append(list(map(int, list(input("Line %d: " %i))[:9])))
    print("Your Puzzle is: ")
    for i in range(9): print(puzzle[i])
    print("The Solution is: ")
    soln = solve(puzzle)
    for i in range(9): print(soln[i])

main()
