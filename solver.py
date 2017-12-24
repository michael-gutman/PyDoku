# solver.py
examplePuzz = [
            [0, 1, 0, 2, 0, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 6, 1, 0, 0],
            [0, 0, 4, 0, 0, 0, 0, 2, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 5, 0],
            [1, 8, 0, 9, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 6, 0],
            [0, 0, 1, 0, 7, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 5, 0]]

def filled(puzzle):
    '''Determines if the puzzle is entirely filled.'''
    for row in puzzle:
        if 0 in row: return False
    return True

def firstUnused(puzzle):
    '''Returns the [row, col] of the topmost-leftmost 0 in puzzle'''
    for i, row in enumerate(puzzle):
        zeroAt = row.index(0)
        if zeroAt > -1:
            return [i, zeroAt]

def addNum(puzzle):
    '''Returns a list of puzzles with the firstUnused(puzzle) replaced with
    1 through 9
    '''
    unused = firstUnused(puzzle)
    row = unused[0]
    col = unused[1]
    res = []
    for i in range(1, 10):
        valid = True
        for j in puzzle[row]:
            if j == i:
                valid = False
                continue
        if not valid: continue
        for j in range(len(puzzle)):
            if puzzle[j][col] == i:
                valid = False
                continue
        if not valid: continue
        r = [puzzle[j][:] for j in range(len(puzzle))]
        r[row][col] = i
        res.append(r)
    return res
