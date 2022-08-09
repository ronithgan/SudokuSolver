from collections import defaultdict
from tracemalloc import start
#Hello World
print("Welcome to Online Sudoku!")

#Add print sudoku board after input and after output

#Enter Input
def enterInput() -> list[list[str]]:
    sudokuBoard = []
    for i in range(9):
        print("Line", i+1, "-->")
        val = input("Please enter the values for this line with no spaces, place a 0 for empty values: ")
        sudokuLine = []
        for x in val:
            sudokuLine.append(int(x))
        sudokuBoard.append(sudokuLine)
    return sudokuBoard

#Valid SudokuBoard
def isValidBoard(sudokuBoard) -> bool:
    rowCheck = defaultdict(set)
    colCheck = defaultdict(set)
    gridCheck = defaultdict(set)
    for r in range(0,len(sudokuBoard)):
        for c in range(0,len(sudokuBoard[0])):
            currVal = int(sudokuBoard[r][c])
            if(currVal>=1 and currVal<10):
                if(currVal in rowCheck[r] or currVal in colCheck[c] or currVal in gridCheck[(r//3, c//3)]):
                    return False
                rowCheck[r].add(currVal)
                colCheck[c].add(currVal)
                gridCheck[(r//3, c//3)].add(currVal)
    return True

#Print Sudoku Board
def printBoard(sudokuBoard):
    for r in range(0,len(sudokuBoard)):
        if r%3 == 0:
            print("- - - - - - - - - - - - - - - - - - -")
        for c in range(0,len(sudokuBoard[0])):
            if c%3==0:
                print("|  ", end = "")
            if c!=8:
                print(sudokuBoard[r][c], " ", end = "")
            else:
                print(sudokuBoard[r][c], " |", end = "")
        print("")
    print("- - - - - - - - - - - - - - - - - - -")
        
#Find Empty Space
def isSolved(sudokuBoard):
    for r in range(0,len(sudokuBoard)):
        for c in range(0,len(sudokuBoard[0])):
            if sudokuBoard[r][c]==0:
                return (r, c)
    return None


#Check if number can be inserted at a given index
def validAdd(sudokuBoard, insertVal, posToInsert):
    #Traverse Row
    for c in range(0, len(sudokuBoard[0])):
        if(sudokuBoard[posToInsert[0]][c]==insertVal and posToInsert[1]!=c):
            return False
    
    #Traverse Column
    for r in range(0, len(sudokuBoard)):
        if(sudokuBoard[r][posToInsert[1]]==insertVal and posToInsert[0]!=r):
            return False
    
    #Traverse Grid
    startCoords = getGrid(posToInsert)
    xStart = startCoords[0]
    yStart = startCoords[1]
    for r in range(yStart, yStart+3):
        for c in range(xStart, xStart+3):
            if sudokuBoard[r][c]==insertVal and posToInsert!=(r,c):
                return False
    
    return True

#Get coordinates to traverse through grid
def getGrid(position):
    xVal = (position[1]//3) * 3
    yVal = (position[0]//3) * 3
    return (xVal, yVal)

#Backtracking to Solve Game
def solveBoard(sudokuBoard):
    emptySquare = isSolved(sudokuBoard)
    if not emptySquare:
        return True
    else:
        row = emptySquare[0]
        col = emptySquare[1]
    
    for x in range(1, 10):
        if validAdd(sudokuBoard, x, (row, col)):
            sudokuBoard[row][col] = x
            if solveBoard(sudokuBoard):
                return True
            sudokuBoard[row][col] = 0
    return False


def runGame():
    #Choose Sudoku Board
    sudokuBoard = enterInput()

    if isValidBoard(sudokuBoard):
        print("This is the original board:")
        printBoard(sudokuBoard)
        print("Solving Board...")
        solveBoard(sudokuBoard)
        print("This is the solved board:")
        printBoard(sudokuBoard)
    else:
        print("This is not a valid Sudoku Board")
        playAgain = input("Enter X if you would like to try again: ")
        if playAgain == 'X'  or playAgain == 'x':
            runGame()


runGame()
