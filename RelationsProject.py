from typing import Set
import random

Space = "    "


def input2set(A, Rsize, raw):
    Rset = []
    counter = 2
    j = 0
    for i in range(Rsize):
        Rset.append([0, 0])

    for i in range(len(raw)):
        if raw[i] in A and counter % 2 == 0 and j < Rsize:
            Rset[j][0] = raw[i]
            counter = counter + 1
        elif raw[i] in A and counter % 2 != 0 and j < Rsize:
            Rset[j][1] = raw[i]
            counter = counter + 1
            j = j + 1

    return Rset


def set2matrix(a, r_set):
    R = MatrixIdentify(len(a))
    for i in range(len(r_set)):
        u = a.index(r_set[i][0])
        v = a.index(r_set[i][1])
        R[u][v] = 1
    return R


def booleanProd(u, v):
    rows = len(u)
    cols = len(v)
    s = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)

        s.append(col)

    for i in range(len(u)):
        s[i].clear()
        for j in range(len(v)):
            isEqual = False

            for k in range(len(u)):

                if u[i][k] == 1 and v[k][j] == 1:
                    isEqual = True

            if isEqual:
                s[i].append(1)

            if not isEqual:
                s[i].append(0)

    return s


def Inverse(r):
    r_inverse = MatrixIdentify(len(r))
    for i in range(len(r)):
        r_inverse[i].clear()
        for j in range(len(r)):
            r_inverse[i].append(r[j][i])

    return r_inverse


def Compliment(r):
    r_compliment = MatrixIdentify(len(r))
    for i in range(len(r)):
        for j in range(len(r)):
            if r[i][j] == 1:
                r_compliment[i][j] = 0
            else:
                r_compliment[i][j] = 1

    return r_compliment


def Union(r, s):
    union_matrix = MatrixIdentify(len(r))

    for i in range(len(r)):
        for j in range(len(r)):
            if r[i][j] == 1 or s[i][j] == 1:
                union_matrix[i][j] = 1

            else:
                union_matrix[i][j] = 0

    return union_matrix


def Intersect(r, s):
    intersect_matrix = MatrixIdentify(len(r))
    for i in range(len(r)):
        for j in range(len(r)):
            if RelationsMatrix[i][j] == 1 and s[i][j] == 1:
                intersect_matrix[i][j] = 1
            else:
                intersect_matrix[i][j] = 0
        print()
    return intersect_matrix


def Matrix2set(A, MR):
    R = []
    for i in range(len(MR)):
        for j in range(len(MR)):
            if MR[i][j] == 1:
                R.append((A[i], A[j]))
    return R


def MatrixIdentify(order):
    rows = order
    cols = order
    m = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        m.append(col)

    return m


def Reflexive(number_of_rows, r):
    is_reflexive = False
    for i in range(number_of_rows):
        if r[i][i] == 1:
            is_reflexive = True
        else:
            is_reflexive = False
            break
    return is_reflexive


def Irreflexive(number_of_rows, r):
    is_irreflexive = False
    for i in range(number_of_rows):
        if r[i][i] == 0:
            is_irreflexive = True
        else:
            is_irreflexive = False
            break
    return is_irreflexive


def Symmetric(number_of_rows, r):
    is_symmetric = False
    temp = 1
    for i in range(number_of_rows):
        if temp == 1:
            for j in range(number_of_rows):
                if r[i][j] == 1 and r[j][i] == 1:
                    is_symmetric = True
                if (r[i][j] == 1 and r[j][i] == 0) or (r[i][j] == 0 and r[j][i] == 1):
                    is_symmetric = False
                    temp = 0
                    break
        else:
            break
    return is_symmetric


def ASymmetric(is_irreflexive, is_anti_symmetric):
    if is_irreflexive == True and is_anti_symmetric == True:
        is_a_symmetric = True
    else:
        is_a_symmetric = False
    return is_a_symmetric


def AntiSymmetric(number_of_rows, r):
    is_anti_symmetric = False
    for i in range(number_of_rows):
        for j in range(number_of_rows):
            if i != j:
                if r[i][j] == 1 and r[j][i] == 1:
                    is_anti_symmetric = False
                    break
                else:
                    is_anti_symmetric = True
    return is_anti_symmetric


def Transitive(r):
    if r == booleanProd(r, r):
        is_transitive = True
    else:
        is_transitive = False
    return is_transitive


def Equivalence(is_transitive, is_reflexive, is_symmetric):
    if is_transitive == True and is_reflexive == True and is_symmetric == True:
        is_equivalence = True
    else:
        is_equivalence = False
    return is_equivalence


def MatrixInputR(set_a):
    while True:
        print("\nWould you like to enter the set R (1) or, the relations matrix (2) : ")
        user_input = input()
        print()

        if user_input == "1":
            MatrixSize = int(input("Enter Set R Size: "))
            print()
            raw_input = ""
            for i in range(MatrixSize):
                print("Enter the related pair number " + str(i + 1) + " (example, (a,b)) :")
                raw_input = raw_input + (input())
                print()
            MatrixSet = input2set(set_a, MatrixSize, raw_input)

            Matrix = set2matrix(set_a, MatrixSet)

            print()
            print("Set R: ", MatrixSet, )
            break

        elif user_input == "2":
            numberOfRows = len(set_a)
            Matrix = MatrixIdentify(numberOfRows)

            for i in range(numberOfRows):
                Matrix[i].clear()
                for j in range(numberOfRows):
                    print("Enter the Element at R \033[33m'(", i + 1, ",", j + 1, ")'\033[0m :")

                    if input() == "1":
                        Matrix[i].append(int(1))
                    else:
                        Matrix[i].append(int(0))
                print()
            break
        else:
            print("\n\033[31mPlease Enter a value between '1' and '2'\033[0m\n")
            continue
    return Matrix


def MatrixInputS(set_a):
    while True:
        print("\nWould you like to enter the set S (1) or, the relations matrix (2) : ")
        user_input = input()
        print()

        if user_input == "1":
            MatrixSize = int(input("Enter Set S Size: "))
            print()
            raw_input = ""
            for i in range(MatrixSize):
                print("Enter the related pair number " + str(i + 1) + " (example, (a,b)) :")
                raw_input = raw_input + (input())
                print()
            MatrixSet = input2set(set_a, MatrixSize, raw_input)

            Matrix = set2matrix(set_a, MatrixSet)

            print()
            print("Set S: ", MatrixSet, )
            break  #

        elif user_input == "2":
            numberOfRows = len(set_a)
            Matrix = MatrixIdentify(numberOfRows)

            for i in range(numberOfRows):
                Matrix[i].clear()
                for j in range(numberOfRows):
                    print("Enter the Element at S \033[33m'(", i + 1, ",", j + 1, ")'\033[0m :")

                    if input() == "1":
                        Matrix[i].append(int(1))
                    else:
                        Matrix[i].append(int(0))
                print()
            break
        else:
            print("\n\033[31mPlease Enter a value between '1' and '2'\033[0m\n")
            continue
    return Matrix


def printMatrix(r):
    print()
    for i in range(len(r)):
        for j in range(len(r)):
            if r[i][j] == 1:
                print("\033[32m", r[i][j], "\033[0m", end=' ')
            else:
                print("\033[31m", r[i][j], "\033[0m", end=' ')
        print()

    print()


def degreesTable(set_size):
    degrees_table = []
    for i in range(2):
        col = []
        for j in range(set_size):
            col.append(0)
        degrees_table.append(col)

    for i in range(set_size):
        for j in range(set_size):
            if RelationsMatrix[i][j] == 1:
                degrees_table[0][j] = degrees_table[0][j] + 1

    for i in range(set_size):
        for j in range(set_size):
            if RelationsMatrix[j][i] == 1:
                degrees_table[1][j] = degrees_table[1][j] + 1
    return degrees_table


def VTHNtable(A, R):
    Table = []
    Vertex = []
    for i in range(len(A)):
        Vertex.append(0)
    Tail = []
    Head = []

    # Making a list for heads and tails
    for i in range(len(R)):
        Tail.append(R[i][0])
    for i in range(len(R)):
        Head.append(R[i][1])

    # Making the Main list called Table that will be printed
    for i in range(len(R)):
        Table.append([Tail[i], Head[i]])
    random.shuffle(Table)
    for i in range(len(R)):
        Table[i].insert(0, i + 1)

    # Making the Vertix list
    for i in range(len(A)):
        for j in range(len(R)):
            if A[i] == Table[j][1]:
                Vertex[i] = Table[j][0]
                break

    # adding new coloumn to Taple that will be the 'Next' Column
    for i in range(len(R)):
        Table[i].append(0)

    # algorithim to find the next element
    for i in range(len(R)):
        for j in range(len(R)):
            if Table[i][1] == Table[j][1] and Table[j][0] not in Vertex and Table[j][3] == 0 and i != j:
                Table[i][3] = Table[j][0]
                break

    # Printer
    print("\n|Vertex|        Index             |               Tail    "
          "           |               Head              |              Next\n")
    for i in range(len(R)):
        if i <= 9:
            if i < len(A):
                print(" " * 3 + str(A[i]) + "|0" + str(Vertex[i]) + "|" + 2 * Space + "0" + str(
                    Table[i][0]) + 4 * Space + "| " + 4 * Space + str(Table[i][1]) + 4 * Space + "|" + 4 * Space + str(
                    Table[i][2]) + 4 * Space + "|" + 4 * Space + str(Table[i][3]) + 4 * Space)
            else:
                print(4 * Space + "0" + str(Table[i][0]) + 4 * Space + "| " + 4 * Space + str(
                    Table[i][1]) + 4 * Space + "|" + 4 * Space + str(Table[i][2]) + 4 * Space + "|" + 4 * Space + str(
                    Table[i][3]) + 4 * Space)
        else:
            if i < len(A):
                print(" " * 3 + str(A[i]) + "|" + str(Vertex[i]) + "| " + 2 * Space + " " + str(
                    Table[i][0]) + 4 * Space + "|" + 4 * Space + str(Table[i][1]) + 4 * Space + "|" + 4 * Space + str(
                    Table[i][2]) + 4 * Space + "|" + 4 * Space + str(Table[i][3]) + 4 * Space)
            else:
                print(4 * Space + str(Table[i][0]) + 4 * Space + "| " + 4 * Space + str(
                    Table[i][1]) + 4 * Space + "|" + 4 * Space + str(Table[i][2]) + 4 * Space + "|" + 4 * Space + str(
                    Table[i][3]) + 4 * Space)


print()
print("**************************************** Program Started ***************************************")
A = []
Asize = int(input("Enter Set A Size: "))
print()
for i in range(0, Asize):
    print("Enter the element at index", i, )
    item = (input())
    A.append(item)

RelationsMatrix = MatrixInputR(A)
MatrixOrder = len(RelationsMatrix)

print("\n")
print("**************************************** Relation Matrix **************************************")
print("\nMatrix R = \n")
printMatrix(RelationsMatrix)
print("************************************** Relation Proporties **************************************")

isReflexive = Reflexive(MatrixOrder, RelationsMatrix)
isIrreflexive = Irreflexive(MatrixOrder, RelationsMatrix)
isAntiSymmetric = AntiSymmetric(MatrixOrder, RelationsMatrix)
isSymmetric = Symmetric(MatrixOrder, RelationsMatrix)
isASymmetric = ASymmetric(isIrreflexive, isAntiSymmetric)
isTransitive = Transitive(RelationsMatrix)
isEquivalence = Equivalence(isTransitive, isReflexive, isSymmetric)

print()
if isReflexive:
    print("\033[0mis Matrix R Reflexive:   \033[32m", isReflexive)
else:
    print("is Matrix R Reflexive:   \033[31m", isReflexive)
if isIrreflexive:
    print("\033[0mis Matrix R Irreflexive: \033[32m", isIrreflexive)
else:
    print("\033[0mis Matrix R Irreflexive: \033[31m", isIrreflexive)
if isSymmetric:
    print("\033[0mis Matrix R Symetric:    \033[32m", isSymmetric)
else:
    print("\033[0mis Matrix R Symetric:    \033[31m", isSymmetric)
if isASymmetric:
    print("\033[0mis Matrix R ASymertric:  \033[32m", isASymmetric)
else:
    print("\033[0mis Matrix R ASymertric:  \033[31m", isASymmetric)
if isAntiSymmetric:
    print("\033[0mis Matrix R AntiSymtric: \033[32m", isAntiSymmetric)
else:
    print("\033[0mis Matrix R AntiSymtric: \033[31m", isAntiSymmetric)
if isTransitive:
    print("\033[0mis Matrix R Transitive:  \033[32m", isTransitive)
else:
    print("\033[0mis Matrix R Transitive:  \033[31m", isTransitive)
if isEquivalence:
    print()
    print("\033[0mMatrix R is an Equivalence Relation")
else:
    print()
    print("\033[0mMatrix R is \033[31mnot\033[0m an Equivalence Relation")

print("**************************************** Matrix Operations ****************************************")

while True:
    print("\nWhat operation do you want to find?")
    print("\033[33m1)\033[0m  find the Relation R on any given order")
    print("\033[33m2)\033[0m  find M R^inf")
    print("\033[33m3)\033[0m  find the compliment of the Matrix")
    print("\033[33m4)\033[0m  find the inverse of the matrix")
    print("\033[33m5)\033[0m  find the union of Matrix R and Matrix S(input)")
    print("\033[33m6)\033[0m  find the intersect of Matrix R and Matrix S(input)")
    print("\033[33m7)\033[0m  find the boolean product of Matrix R and Matrix S(input)")
    print("\033[33m8)\033[0m  find the in degrees and out degrees table")
    print("\033[33m9)\033[0m  find the VERT TAIL HEAD NEXT table")
    print("\n"
          "\033[31m0)\033[0m  Exit the program\n")
    userOpInput = input("Enter the index of the desired operation: ")

    Power = [RelationsMatrix]

    for i in range(1, MatrixOrder):
        Power.append(booleanProd(RelationsMatrix, Power[i - 1]))

    if userOpInput == "1":
        n = int(input("\nEnter The Number of The Power of MR You Want: "))
        order = n%MatrixOrder

        print("Matrix R^", n, "= \n")
        for i in range(len(Power[order - 1])):
            for j in range(len(Power[order - 1][i])):
                if Power[order - 1][i][j] == 1:
                    print("\033[32m", Power[order - 1][i][j], "\033[0m", end=' ')
                else:
                    print("\033[31m", Power[order - 1][i][j], "\033[0m", end=' ')
            print()
        print("\n"
              "***********************************************************************************************")

    if userOpInput == "2":

        powerInf = MatrixIdentify(MatrixOrder)
        for i in range(MatrixOrder - 1):
            powerInf = Union(powerInf, Power[i])
        print("\nMatrix R^inf = \n")
        printMatrix(powerInf)

        print("\n***********************************************************************************************")

    if userOpInput == "3":
        RComp = Compliment(RelationsMatrix)
        print("\nCompliment of Matrix R = ")
        printMatrix(RComp)

        print("\n***********************************************************************************************")

    if userOpInput == "4":
        RInverse = Inverse(RelationsMatrix)
        print("\nInverse of Matrix R = ")
        printMatrix(RInverse)

        print("\n***********************************************************************************************")

    if userOpInput == "5":
        S = MatrixInputS(A)
        MRUS = Union(RelationsMatrix, S)
        print("Matrix R =")
        printMatrix(RelationsMatrix)
        print("Matrix S =")
        printMatrix(S)
        print("\nMatrix R union S = ")
        printMatrix(MRUS)

        print("\n***********************************************************************************************")

    if userOpInput == "6":
        S = MatrixInputS(A)
        MRIS = Intersect(RelationsMatrix, S)
        print("Matrix R =")
        printMatrix(RelationsMatrix)
        print("Matrix S =")
        printMatrix(S)
        print("Matrix R intersect S = ")
        printMatrix(MRIS)

        print("\n***********************************************************************************************")
    if userOpInput == "7":
        S = MatrixInputS(A)

        while True:
            print("Would you to find MatrixR X MatrixS (1) or MatrixS X MatrixR (2) ?")
            userProductInput = str(input())
            print()
            if userProductInput == "1":
                print("Matrix R =")
                printMatrix(RelationsMatrix)
                print("Matrix S =")
                printMatrix(S)
                print("the Boolean product of MatrixR on MatrixS =")
                printMatrix(booleanProd(RelationsMatrix, S))
                break
            elif userProductInput == "2":
                print("Matrix R =")
                printMatrix(RelationsMatrix)
                print("Matrix S =")
                printMatrix(S)
                print("the Boolean product of MatrixS on MatrixR =")
                printMatrix(booleanProd(S, RelationsMatrix))
                break
            else:
                print("\n\033[31mPlease Enter a value between '1' and '2'\033[0m\n")

        print("\n***********************************************************************************************")

    if userOpInput == "8":
        degrees = degreesTable(MatrixOrder)

        print("in degrees and out degrees table: ")
        print()
        for i in range(2):
            if i == 0:
                print("in degree:  ")
            else:
                print("out degree: ")
            for j in range(MatrixOrder):
                print("\033[32m", degrees[i][j], "\033[0m", end=' ')
            print()

        print("\n***********************************************************************************************")
    if userOpInput == "9":
        print("\nSet R:\n")
        SetR = Matrix2set(A, RelationsMatrix)
        print(SetR)
        VTHNtable(A, SetR)
    if userOpInput == "0":
        break

print("\n\n")
print("**************************************** Program Ended ****************************************")
