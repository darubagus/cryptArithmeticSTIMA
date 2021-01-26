
import time

# listOfNode = [{letter, corresponding value}]
use = [0 for i in range(10)]

listOfWord = []
listOfNode = []
opCounter = 1


def noLeadingZero(listOfWord):
    noZero = []
    for i in range(len(listOfWord)):
        noZero.append(listOfWord[i][0])

    return noZero

def isValid(listOfNode, countChar, listOfWord) :
    global val 
    global opCounter
    val = [0 for i in range(len(listOfWord))]
    temp = 0
    totalVal=0

    for z in range(len(listOfWord)):
        m = 1
        i = len(listOfWord[z])-1
        while (i >= 0) :
            char = listOfWord[z][i]
            for j in range(countChar) :
                temp = j
                if (listOfNode[j][0] == char) :
                    break
            val[z] += m * listOfNode[temp][1]
            m *= 10
            i-=1
    
    # buat ngecek hasil
    for i in range(len(listOfWord)-1) :
        totalVal += val[i]
    
    if (totalVal == val[len(listOfWord)-1]) :
        return True
    else:
        opCounter += 1
        return False


def Permutate(uniqueChar, listOfNode, n, listOfWord) :
    global opCounter
    if (n == uniqueChar-1):#Basis
        if ((listOfNode[n][0] not in(noLeadingZero(listOfWord)))) :
            for i in range(10):
                if (use[i] == 0):
                    listOfNode[n][1] = i
                    if (isValid(listOfNode,uniqueChar,listOfWord)) :
                        return True
        else :
            for i in range(1,10):
                if (use[i] == 0):
                    listOfNode[n][1] = i
                    if (isValid(listOfNode,uniqueChar,listOfWord)) :
                        return True
    else:
        if (listOfNode[n][0] not in(noLeadingZero(listOfWord))):
            for i in range(10):
                if (use[i]==0):
                    listOfNode[n][1] = i
                    use[i] = 1
                    if (Permutate(uniqueChar,listOfNode, n+1,listOfWord)):
                        return True
                    use[i] = 0
        else :
            for i in range(1,10):
                if (use[i]==0):
                    listOfNode[n][1] = i
                    use[i] = 1
                    if (Permutate(uniqueChar,listOfNode, n+1,listOfWord) ):
                        return True
                    use[i] = 0

def problemSolver(listofWord,listOfNode):
    uniqueChar = 0
    
    letterFrequency = [0 for i in range(26)]

    for i in range(len(listOfWord)):
        for j in range(len(listOfWord[i])):
            letterFrequency[ord(listOfWord[i][j]) - ord('A')] += 1

    for i in range(26):
        if (letterFrequency[i] > 0) :
            uniqueChar +=1
    
    if (uniqueChar > 10) :
        # Operand terlalu banyak
        print("Invalid input")
    
    # listOfNode = [{letter, corresponding value}]
    listOfNode = []

    for i in range(26):
        j = 0
        if (letterFrequency[i] > 0) :
            # listOfNode[j][0] = chr(i + ord('A'))
            # [['A',0]]
            listOfNode.append([chr(i + ord('A')), 0])
            j += 1
            # listOfNode.append([chr(i + ord('A')), 0])


    return Permutate(uniqueChar, listOfNode, 0, listOfWord)

def displayAngka() : 
    for i in range(len(listOfWord)-1):
        if (i != len(listOfWord)-2):
            txt = str(val[i]).rjust(8)
            print(txt)
        else :
            txt = str(val[i]).rjust(8)
            print(txt+"+")

    length = (len(max(listOfWord, key=len)))
    string = ''
    for i in range(length) :
        string += '-'
    string = string.rjust(8)
    print(string)

    txt = str(val[len(listOfWord)-1]).rjust(8)
    print(txt)
    print("\n")

def displayWord(listOfWord):
    for i in range(len(listOfWord)-1):
        if (i != len(listOfWord)-2):
            txt = (listOfWord[i]).rjust(8)
            print(txt)
        else :
            txt = (listOfWord[i]).rjust(8)
            print(txt+"+")

    length = (len(max(listOfWord, key=len)))
    string = ''
    for i in range(length) :
        string += '-'
    string = string.rjust(8)
    print(string)

    txt = (listOfWord[len(listOfWord)-1]).rjust(8)
    print(txt)
    print("\n")

#MAIN PROGRAM

# open file
fileName = input("Masukkan nama file (sama extensionnya ya) : ")
problem = "../test/"+fileName
inString = open(problem, "r")

# inString = open("money.txt", "r")
line = inString.readlines()

i = 0
while (i < len(line)):
    if (line[i][0] != '-'):
        # do nothing
        cleanString = line[i].replace(" ","")
        cleanString = cleanString.replace("+","")
        cleanString = cleanString.replace("\n","")
        
        listOfWord.append(cleanString)
    i+=1
inString.close()

# START TIME
startTime = time.time()
problemSolver(listOfWord,listOfNode)
# print(problemSolver(listOfWord))

# print(problemSolver(listOfWord))
print("\n")
displayWord(listOfWord)
displayAngka()
# HITUNG RUNNING TIME
runningTime = (time.time() - startTime)
print("Total percobaan  : "+str(opCounter))
print("Waktu dibutuhkan : %.2f sec(s)" %(runningTime))
