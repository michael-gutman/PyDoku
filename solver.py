# solver.py
examplePuzz = [
            [0, 1, 0, 2, 0, 0, 0, 3, 0]
            [2, 0, 0, 0, 0, 6, 1, 0, 0]
            [0, 0, 4, 0, 0, 0, 0, 2, 0]
            [0, 2, 0, 0, 0, 0, 0, 0, 1]
            [0, 0, 0, 0, 1, 0, 0, 5, 0]
            [1, 8, 0, 9, 0, 2, 0, 0, 0]
            [0, 0, 2, 0, 0, 0, 0, 6, 0]
            [0, 0, 1, 0, 7, 0, 0, 0, 0]
            [4, 0, 0, 0, 0, 0, 0, 5, 0]]

def filled(puzzle):
    '''Determines if the puzzle is entirely filled.'''
    for e in enumerate(puzzle):
        if 0 in e: return False
    return True
