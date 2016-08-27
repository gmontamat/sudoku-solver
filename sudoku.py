# Sudoku Solver

def toTuple(userin):
    sudoku = ()
##    # HTS sudoku format
##    i = 0
##    while i<len(userin):
##        if userin[i] == ',':
##            sudoku = sudoku + ((1,2,3,4,5,6,7,8,9),)
##        else:
##            sudoku = sudoku + ((int(userin[i]),),)
##            i = i + 1 # Skips next comma
##        i = i + 1
    i = 0
    while i<len(userin):
        if userin[i] == '.':
            sudoku = sudoku + ((1,2,3,4,5,6,7,8,9),)
        else:
            sudoku = sudoku + ((int(userin[i]),),)
        i = i + 1
    return sudoku

def solveSudoku(sudoku):
    modified = True
    noSolution = False
    while (modified == True):
        modified = False
        for i in range(len(sudoku)):
            # Check every cell
            if len(sudoku[i])>0:
                # Erase elements which appear on same row, column or square
                eraseList = getEraseList(sudoku, i)
                newcell = ()
                for element in sudoku[i]:
                    if element not in eraseList:
                        newcell = newcell + (element,)
                if newcell != sudoku[i]:
                    modified = True
                    temp = sudoku
                    sudoku = ()
                    for j in range(len(temp)):
                        if j != i:
                            sudoku = sudoku + (temp[j],)
                        else:
                            sudoku = sudoku + (newcell,)
            # When this function guess a value for a cell and calls itself
            # an impossible sudoku may appear. In that case an empty tuple
            # (len(sudoku[i]==0) will show up.
            else:
                noSolution = True
                modified = False
                break
    if checkSolved(sudoku) == False and noSolution == False:
        minindexlen = 10
        for i in range(len(sudoku)):
            if len(sudoku[i]) > 1 and len(sudoku[i]) < minindexlen:
                index = i
                minindexlen = len(sudoku[i])
        for number in sudoku[index]:
            #print index, sudoku[index], number
            #print sudoku
            #print 'I call myself'
            temp = sudoku
            sudoku = ()
            for j in range(len(temp)):
                if j != index:
                    sudoku = sudoku + (temp[j],)
                else:
                    sudoku = sudoku + ((number,),)
            solveSudoku(sudoku)
    elif noSolution == False:
        # An answer was found
        #printSudoku(sudoku)
        print toString(sudoku)

def toString(sudoku):
    solution = ''
    for i in range(len(sudoku)):
        solution = solution + str(sudoku[i][0])
    return solution

def getEraseList(sudoku, i):
    # PLEASE IMPROVE THIS CODE
    eraseList = []
    # Get indexes from same row cells
    indexList = range((i/9)*9, (i/9)*9+9)
    indexList.remove(i)
    # Add indexes from same column cells
    cell = i % 9
    while (cell<81):
        if cell != i and cell not in indexList:
            indexList.append(cell)
        cell = cell + 9
    # Add indexes from same square list
    square = [[0,1,2,9,10,11,18,19,20],[27,28,29,36,37,38,45,46,47],[54,55,56,63,64,65,72,73,74],
              [3,4,5,12,13,14,21,22,23],[30,31,32,39,40,41,48,49,50],[57,58,59,66,67,68,75,76,77],
              [6,7,8,15,16,17,24,25,26],[33,34,35,42,43,44,51,52,53],[60,61,62,69,70,71,78,79,80]]
    for j in range(len(square)):
        if i in square[j]:
            square[j].remove(i)
            for index in square[j]:
                if index not in indexList:
                    indexList.append(index)
    for index in indexList:
        for number in sudoku[index]:
            if len(sudoku[index])== 1 and number not in eraseList:
                eraseList.append(number)
    return eraseList

def checkSolved(sudoku):
    solved = True
    for i in range(len(sudoku)):
        if len(sudoku[i]) != 1:
            solved = False
            break
    return solved

def checkInput(userin):
    if len(userin) != 81:
        return False
    else:
        correct = True
        for i in range(len(userin)):
            char = userin[i]
            if char.isdigit() == False and char!='.':
                correct = False
                break
        return correct

##def printSudoku(sudoku):
##    for i in range(81):
##        print sudoku[i][0],
##        if i % 9 == 8:
##            print

# HTS sudoku format
#userin = '9,3,6,,,8,7,1,4,1,4,7,6,,,,2,5,,,,7,4,,,,6,6,9,3,,,5,4,7,1,,,,,9,,5,8,,8,,5,,1,7,6,,3,,,,1,,4,3,6,9,4,7,1,9,6,3,2,5,8,,,9,,,2,1,4,7'
#userin = ',2,5,7,1,4,6,,9,9,,,,2,,,4,1,,4,7,9,3,6,8,,2,5,8,,,,1,3,,6,6,9,3,,8,2,4,1,7,7,,,6,,,5,2,8,4,,1,3,,,,8,5,3,,9,,5,,,7,,,5,8,1,,7,9,,3'
# Traditional sudoku format
#userin = '8..6..9.5.............2.31...7318.6.24.....73...........279.1..5...8..36..3......'
# Extreme sudoku
#userin = '6.7.9.5.4....4....9..7.6..2..5...2..38.....46..9...8..5..4.2..9....1....7.6.3.4.5'
# World's hardest sudoku
#userin = '8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..'
userin = raw_input('Enter sudoku: ')
if checkInput(userin) == False:
    print 'Wrong format'
else:
    sudoku = toTuple(userin)
    print 'Looking for solutions...'
    solveSudoku(sudoku)
    print 'Done'
