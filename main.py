#AI project........
#We certify that this submission is the original work of members of the group and meets the Faculty's Expectations of Originality
#Jamila Fawaqa 1200435
#Hala Gholeh 1201418
import numpy as np
#FUNCTION TO CONVERT THE USER INPUT TO INDEX OF THE ARRAY

leastRow = None
leastCOL = None
list = []
def covertUserPosition(userPos):
    global leastRow
    global leastCOL
    row = None
    colomn = None

    if userPos == "H1":
        return 7, 0

    if len(userPos) < 2 :
        print("Illegal input! try again...\n")
        return None, None
    else:
        if userPos[0] in 'ABCDEFGH':
            colomn = ord(userPos[0]) - 65
        if userPos[1] in '12345678':
            row = int(userPos[1]) - 1
        if colomn is not None and row is not None:
            leastRow = row
            leastCOL = colomn
            return colomn, row
        else:
            print("Illegal input! try again...\n")
            return None, None

#FUNCTION TO CHECK IF THE USER INPUT IS LEGAL
def checkIfPositionllegal(row, colomn):
    global bord
    if colomn == 0 or colomn == 7:
        if row in range(0,8):
            if bord[row][colomn] == '[ ]':
                return True
        else:
            return False
    elif row == 0 and (bord[row][colomn-1] != '[ ]' or bord[row][colomn+1] != '[ ]' or bord[row+1][colomn] != '[ ]'):
        return True
    elif row == 7 and (bord[row-1][colomn] != '[ ]' or bord[row][colomn-1] != '[ ]' or bord[row][colomn+1] != '[ ]'):
        return True
    elif row in range (1,7) and (bord[row-1][colomn] != '[ ]' or bord[row][colomn-1] != '[ ]' or bord[row][colomn+1] != '[ ]' or bord[row+1][colomn] != '[ ]'):
        return True
    else:
        return False

def readFromUser(player):
    print("enter the position of your mag:\n")
    userPos = input()

    colomn, row = covertUserPosition(userPos)
    flag = checkIfPositionllegal(row, colomn)
    if flag == True and player == 1:
        bord[row][colomn] = '[■]'
        return True
    elif flag == True and player == 2:
        bord[row][colomn] = '[□]'
        return True
    else:
        print("illegal input! try again...\n")
        return False

#FUNCTION CHECK IF THE BORD IS FULL
def bordIsFull():
    global bord
    for row in bord:
        for element in row:
            if element == '[ ]':
                return False
    return True
def rowIsFull(i):
    global bord
    count = 0
    for row in bord:
        if i == count:
            for content in row:
                if content == '[ ]':
                    return False
        else:
            count += 1
    return True

def checkForVerticalWin(player):
    global bord
    counter = 0
    content = ''
    if player == 1 :
        content = '[■]'
    else:
        content = '[□]'
    num_rows = len(bord)
    num_cols = len(bord[0])

    for col in range(num_cols):
        for row in range(num_rows):
            element = bord[row][col]
            if element == content:
                counter = counter+1
                if counter == 5:
                    return counter
            else:

                counter = 0
    return counter
    #return False

#############################################
def winV(content, listC):
    global bord
    num_rows = len(bord)
    num_cols = len(bord[0])
    counter = 0

    for col in range(num_cols):
        if col not in listC:
            counter = 0
            for row in range(num_rows):
                element = bord[row][col]
                if element == content:
                    counter += 1
                else:
                    counter = 0

                if counter == 3:
                    listC.append(col)
                    return True

    return False


##############################################
def checkForHorizontalWin(player):
    global bord
    counter = 0
    content = ''
    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    for row in bord:
        for element in row:
            if element == content:
                counter = counter + 1
                if counter == 5:
                    return counter
            else:

                counter = 0
    return counter
    #return False
def checkForDownDiagonalWin(player):
    global bord
    counter = 0
    content = ''
    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    for row in range(len(bord)):
        for col in range(len(bord[row])):
            i = row
            j = col
            if bord[row][col] == content:
                counter += 1
                while counter != 0:
                    try:
                        if row + 1 < len(bord) and col + 1 < len(bord[row]):
                            i += 1
                            j += 1
                            if bord[i][j] == content:
                                counter += 1
                                if counter == 5:
                                    return counter
                            else:
                                #return counter
                                counter = 0
                        else:
                            #return counter
                            counter = 0
                    except IndexError:
                        #return counter
                        counter = 0

            else:
                #return counter
                counter = 0

    return counter
    #return False

def checkForUpperDiagonalWin(player):
    global bord
    counter = 0
    content = ''
    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    for row in range(len(bord)):
        for col in range(len(bord[row])):
            if bord[row][col] == content:
                counter += 1
                while counter != 0:
                    try:
                        if bord[row - 1][col + 1] == content:
                            row -= 1
                            col += 1
                            counter += 1
                            if counter == 5:
                                return counter
                        else:
                            #return counter
                            counter = 0
                    except IndexError:
                        #return counter
                        counter = 0
            else:
                #return counter
                counter = 0
    return counter
    #return False

def checkForWinning(player):
    if checkForVerticalWin(player) == 5:
        return True
    elif checkForHorizontalWin(player) == 5:
        return True
    elif checkForDownDiagonalWin(player) == 5:
        return True
    elif checkForUpperDiagonalWin(player) == 5:
        return True
    else:
        return False
#FUNCTION TO PRINT THE BORD
def printBord():
    global bord
    print("   A   B   C   D   E   F   G   H")
    count = 1
    for row in bord:
        print(count, end=" ")
        for element in row:
            print(element, end=" ")
        print(count)
        count += 1
    print("   A   B   C   D   E   F   G   H")

def evaluationFunction(player):
    global bord
    if player == 1:
        competitor = 2
    else:
        competitor = 1

    score = 0
    maxScore = 0
    Svertical = checkForVerticalWin(player)
    Shorizontal  = checkForHorizontalWin(player)
    Sdiagonalupp  = checkForUpperDiagonalWin(player)
    Sdiagonadown  = checkForDownDiagonalWin(player)

    maxScore = max(Svertical , Shorizontal , Sdiagonalupp )

    if maxScore == Svertical:
        for row in range(len(bord)):
            for col in range(len(bord[row])):
                score += upperVerticalScore(row, col, player)
                #score -= upperVerticalScore(row, col, competitor)
                score += downVerticalScore(row, col, player)
                #score -= downVerticalScore(row, col, competitor)
        #return score

    elif maxScore == Shorizontal:
        for row in range(len(bord)):
            for col in range(len(bord[row])):
                score += RhorizontalScore(row, col, player)
                #score -= RhorizontalScore(row, col, competitor)
                score += LhorizontalScore(row, col, player)
                #score -= LhorizontalScore(row, col, competitor)
       # return score

    elif maxScore == Sdiagonalupp:
        for row in range(len(bord)):
            for col in range(len(bord[row])):
                score += upDiagonalScoreToTheUp(row, col, player)
                #score -= upDiagonalScoreToTheUp(row, col, competitor)
                score += upDiagonalScoreToTheDown(row, col, player)
                #score -= upDiagonalScoreToTheDown(row, col, competitor)
        #return score

    elif maxScore == Sdiagonadown:
        for row in range(len(bord)):
            for col in range(len(bord[row])):
                score += downDiagonalScoreToTheUp(row, col, player)
                #score -= downDiagonalScoreToTheUp(row, col, competitor)
                score += downDiagonalScoreToTheDown(row, col, player)
                #score -= downDiagonalScoreToTheDown(row, col, competitor)
        #return score
    return score



#calculate vertical score
#The first function of calculate virtical "Down"
def downVerticalScore(row, col, player):
    global ROWS
    global bord

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    counter = 0
    if (row + 4 < ROWS):
        for i in range (5):
            if bord [row + i][col] == content:
                counter += 1
            elif bord [row + i][col] != '[ ]':
                return 0
    else:
        return 0
    return counter
#The second function of calculate virtical "Upper"
def upperVerticalScore(row, col, player):
    global ROWS
    global bord

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    counter = 0
    if (row - 4 > ROWS - (ROWS + 1)):
        for i in range(5):
            if bord[row - i][col] == content:
                counter += 1
            elif bord[row - i][col] != '[ ]':
                return 0
    else:
        return 0
    return counter

#calculate horizontal score
#The first function of calculate horizontal score "Right"
def RhorizontalScore (row , col , player):
    global bord
    global COLOMNS
    counter = 0
    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col + 4 < COLOMNS:
        for i in range (5):
            if bord[row][col + i] == content:
                counter += 1

            elif bord[row][col + i] != '[ ]':
                return 0
    else:
        return 0

    return counter

#The second part of calculation horizontal score "Left"
def LhorizontalScore(row, col, player):
    global bord
    global COLOMNS
    counter = 0
    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col - 4 > COLOMNS - (COLOMNS + 1):
        for i in range(5):
            if bord[row][col - i] == content:
                counter += 1

            elif bord[row][col - i] != '[ ]':
                return 0
    else:
        return 0

    return counter
#calculate diagonal score
#The first function to calculate diagonal score "Down"
def downDiagonalScoreToTheDown (row , col , player):
    global bord
    global COLOMNS
    global ROWS
    counter = 0

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col + 4 < COLOMNS and row + 4 < ROWS :
        for i in range(5):
            if bord[row + i][col + i] == content:
                counter += 1

            elif bord[row + i][col + i] != '[ ]':
                return 0
    else:
        return 0

    return counter

#The second function to calculate diagonal score "Upper"

def downDiagonalScoreToTheUp (row , col , player):
    global bord
    global COLOMNS
    global ROWS
    counter = 0

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col - 4 > COLOMNS - (COLOMNS + 1) and row - 4 > ROWS - (ROWS + 1):
        for i in range(5):
            if bord[row - i][col - i] == content:
                counter += 1

            elif bord[row - i][col - i] != '[ ]':
                return 0
    else:
        return 0

    return counter
def upDiagonalScoreToTheDown(row, col, player):
    global bord
    global COLOMNS
    global ROWS
    counter = 0

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col - 4 > COLOMNS - (COLOMNS + 1) and row + 4 < ROWS:
        for i in range(5):
            if bord[row + i][col - i] == content:
                counter += 1

            elif bord[row + i][col - i] != '[ ]':
                return 0
    else:
        return 0

    return counter
def upDiagonalScoreToTheUp(row, col, player):
    global bord
    global COLOMNS
    global ROWS
    counter = 0

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if col + 4 < COLOMNS and row - 4 > ROWS - (ROWS + 1):
        for i in range(5):
            if bord[row - i][col + i] == content:
                counter += 1

            elif bord[row - i][col + i] != '[ ]':
                return 0
    else:
        return 0

    return counter



def tryMove(left, row, content):
    if(left):
        for col in range(row):
            if bord[row][col] == '[ ]' :
                bord[row][col] = content
                return col
    else:
        for col in range(row, 0 , -1):
            if bord[row][col] == '[ ]':
                bord[row][col] = content
                return col

    return -1

def minNodes(depth, maxValue, player):
    global bord
    global MAX_VALUE
    global MIN_VALUE
    global ROWS

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if (depth == 0 or bordIsFull()):
        return evaluationFunction(player)

    minValue = MAX_VALUE
    for row in range (ROWS):
        #left side of the tree
        if(not rowIsFull(row)):
            col = tryMove(False, row, content)
            if not checkIfPositionllegal(row , col):
                print("")
            score = maxNodes(depth - 1, minValue, player)
            if (checkForWinning(player)):
                bord[row][col] = '[ ]'
                return MIN_VALUE
            if score < maxValue:
                bord[row][col] = '[ ]'
                return score
            if score < minValue:
                minValue = score
            bord[row][col] = '[ ]'

        # right side of the tree
        if (not rowIsFull(row)):
            col = tryMove(True, row, content)
            if not checkIfPositionllegal(row, col):
                print("")
            score = maxNodes(depth - 1, minValue, player)
            if (checkForWinning(player)):
                bord[row][col] = '[ ]'
                return MIN_VALUE
            if score < maxValue:
                bord[row][col] = '[ ]'
                return score
            if score < minValue:
                minValue = score
            bord[row][col] = '[ ]'
    return minValue

def maxNodes(depth, minValue, player):
    global bord
    global MAX_VALUE
    global MIN_VALUE
    global ROWS

    if player == 1:
        content = '[■]'
    else:
        content = '[□]'

    if (depth == 0 or bordIsFull()):
        return evaluationFunction(player)

    maxValue = MIN_VALUE
    for row in range (ROWS):
        #left side of the tree
        if(not rowIsFull(row)):
            col = tryMove(False, row, content)
            if not checkIfPositionllegal(row, col):
                print("")
            score = minNodes(depth - 1, maxValue, player)
            if(checkForWinning(player)):
                bord[row][col] = '[ ]'
                return MAX_VALUE
            if score > minValue:
                bord[row][col] = '[ ]'
                return score
            if score > maxValue:
                maxValue = score
            bord[row][col] = '[ ]'

        # right side of the tree
        if (not rowIsFull(row)):
            col = tryMove(True, row, content)
            if not checkIfPositionllegal(row, col):
                print("")
            score = minNodes(depth - 1, maxValue, player)
            if (checkForWinning(player)):
                bord[row][col] = '[ ]'
                return MAX_VALUE
            if score > minValue:
                bord[row][col] = '[ ]'
                return score
            if score > maxValue:
                maxValue = score
            bord[row][col] = '[ ]'
    return maxValue


#MINIMAX FUNCTION
def minimax (player, depth):
    global flaggg
    global bord
    global MAX_VALUE
    global ROWS
    global MIN_VALUE
    minValue = MAX_VALUE
    maxValue = MIN_VALUE

    bestMoveRow = 0
    bestMoveColomn = 0
    bestMoveScore = 0

    global list
    print(leastRow , "gggggggg")
    H = winV('[■]',list)
    print(H , "hhhhhhhhhhhhhhhh")
    if H :
        bestMoveRow = leastRow + 1
        bestMoveColomn = leastCOL
        list.append(leastCOL)
        return bestMoveRow , bestMoveColomn , bestMoveScore

    for row in range(ROWS):
        #left side
        if not rowIsFull(row):
            col = tryMove(False, row, player)
            if not checkIfPositionllegal(row, col):
                print("")
            score = maxNodes(depth - 1, minValue, player)
            #score = minNodes(depth - 1, maxValue, player)
            if checkForWinning(player):
                bestMoveRow = row
                bestMoveColomn = col
                bestMoveScore = score
                bord[row][col] = '[ ]'
                return bestMoveRow, bestMoveColomn, bestMoveScore
            if score >= maxValue:
                maxValue = score
                bestMoveRow = row
                bestMoveColomn = col
                bestMoveScore = score
            bord[row][col] = '[ ]'

        # right side
        if not rowIsFull(row):
            col = tryMove(False, row, player)
            if not checkIfPositionllegal(row, col):
                print("")
            score = maxNodes(depth - 1, minValue, player)
            #score = minNodes(depth - 1, maxValue, player)
            if checkForWinning(player):
                bestMoveRow = row
                bestMoveColomn = col
                bestMoveScore = score
                bord[row][col] = '[ ]'
                return bestMoveRow, bestMoveColomn, bestMoveScore
            if score >= maxValue:
                maxValue = score
                bestMoveRow = row
                bestMoveColomn = col
                bestMoveScore = score
            bord[row][col] = '[ ]'
    return bestMoveRow, bestMoveColomn, bestMoveScore


#Global variabels
ROWS = 8
COLOMNS = 8
PLAYER1 = 1
PLAYER2 = 2
MIN_VALUE = -1000000
MAX_VALUE = 1000000
DEPTH = 3
#Initialize the bored
bord = np.full((ROWS, COLOMNS), "[ ]")
print ("   A   B   C   D   E   F   G   H")
count = 1
for row in bord:
    print(count,' '.join(row),count)
    count = count+1
print ("   A   B   C   D   E   F   G   H")
print("choose the mood of play:\n1)manul vs manul\n2)manul with ■ vs atoumatically □\n3)manul with □ vs atoumatically ■\n")
choice = input()

if int(choice) == 1:
    while not bordIsFull():
        flag = False
        while not flag:
            print("Player1 turn ...\n")
            printBord()
            flag = readFromUser(PLAYER1)
            if checkForWinning(PLAYER1):  # check for winning
                print("Player1 Wins!\n")
                printBord()
                exit(0)
        flag2 = False
        while not flag2:
            print("Player2 turn ...\n")
            printBord()
            flag2 = readFromUser(PLAYER2)
            if checkForWinning(PLAYER2):  # check for winning
                print("Player2 Wins!\n")
                printBord()
                exit(0)


    print("It Is a TIE!\n")

elif int(choice) == 2:
    while not bordIsFull():
        flag = False
        while not flag:
            print("It Is Your Turn...\n")
            printBord()
            flag = readFromUser(PLAYER1)
            if checkForWinning(PLAYER1):  # check for winning
                print("Player1 Wins!\n")
                printBord()
                exit(0)
        flag = False
        #computer turn
        bestMoveRow, bestMoveColomn, bestMoveScore = minimax(PLAYER2, DEPTH)
        print("score = " + str(bestMoveScore))
        bord[bestMoveRow][bestMoveColomn] = '[□]'
        if checkForWinning(PLAYER2):
            print("Player2 Wins!\n")
            printBord()
            exit(0)

    print("It Is a TIE!\n")
elif int(choice) == 3:
    while not bordIsFull():
        flag = False
        # computer turn
        bestMoveRow, bestMoveColomn, bestMoveScore = minimax(PLAYER1, DEPTH)
        print("score = " + str(bestMoveScore))
        bord[bestMoveRow][bestMoveColomn] = '[■]'
        if checkForWinning(PLAYER1):
            print("Player2 Wins!\n")
            printBord()
            exit(0)
        while not flag:
            print("It Is Your Turn...\n")
            printBord()
            flag = readFromUser(PLAYER2)
            if checkForWinning(PLAYER2):  # check for winning
                print("Player1 Wins!\n")
                printBord()
                exit(0)
        flag = False


    print("It Is a TIE!\n")
else:
    print("invalid choice! try again...\n")