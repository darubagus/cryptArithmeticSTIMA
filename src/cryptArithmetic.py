
import time

# listOfNode = [{letter, corresponding value}]
use = [0 for i in range(10)]

listOfWord = []
listOfNode = []


# MENGECEK APAKAH
def isFirstZero(listOfWord, listOfNode, countChar):
    # cari 0 di index pertama operand
    for i in range(len(listOfWord)-1):
        for j in range(countChar) :
            if ((listOfNode[j][0] == listOfWord[i][0]) and (listOfNode[j][1] == 0)):
                return True

def isValid(listOfNode, countChar, listOfWord) :
    global val 
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
        return False


def Permutate(countChar, listOfNode, n, listOfWord, opCounter) :
    if (n == countChar-1): #Basis
        for i in range(10):
            opCounter += 1
            if (use[i] == 0):
                listOfNode[n][1] = i
                if (isValid(listOfNode,countChar,listOfWord)) :
                    print("Jumlah operasi : "+str(opCounter))
                    return True
    else:
        for i in range(10):
            opCounter += 1
            if (use[i]==0):
                listOfNode[n][1] = i
                use[i] = 1
                if (Permutate(countChar,listOfNode, n+1,listOfWord, opCounter) ):
                    return True
                use[i] = 0
        

def problemSolver(listofWord,listOfNode):
    char = 0
    length = []

    for i in range(len(listOfWord)-1):
        length.append(len(listOfWord[i]))
    
    letterFrequency = [0 for i in range(26)]

    for i in range(len(listOfWord)):
        for j in range(len(listOfWord[i])):
            letterFrequency[ord(listOfWord[i][j]) - ord('A')] += 1

    for i in range(26):
        if (letterFrequency[i] > 0) :
            char +=1
    
    if (char > 10) :
        # Operand terlalu banyak
        print("Invalid input")
    
    # listOfNode = [{letter, corresponding value}]
    listOfNode = []

    for i in range(26):
        j = 0
        if (letterFrequency[i] > 0) :
            # listOfNode[j][0] = chr(i + ord('A'))
            listOfNode.append([chr(i + ord('A')), 9])
            j += 1
            # listOfNode.append([chr(i + ord('A')), 0])
        
    opCounter = 0

    return Permutate(char, listOfNode, 0, listOfWord, opCounter)

def displayAngka() : 
    for i in range(len(listOfWord)-1):
        if (i != len(listOfWord)-2):
            print(val[i])
        else :
            print(str(val[i])+"+")

    length = (len(max(listOfWord, key=len))+1)
    string = ''
    for i in range(length) :
        string += '-'
    print(string)

    print(val[len(listOfWord)-1])
    print("\n")

def displayWord(listOfWord):
    for i in range(len(listOfWord)-1):
        if (i != len(listOfWord)-2):
            print(listOfWord[i])
        else :
            print(listOfWord[i]+"+")

    length = (len(max(listOfWord, key=len)))
    string = ''
    for i in range(length) :
        string += '-'
    print(string)

    print(listOfWord[len(listOfWord)-1])
    print("\n")

#MAIN PROGRAM
# fileName = input("Masukkan nama file :")
# problem = "../test/"+fileName+".txt"
# inString = open(problem, "r")
# open file
fileName = input("Masukkan nama file :")
problem = "../test/"+fileName+".txt"
# inString = open(problem, "r")

inString = open("input.txt", "r")
line = inString.readlines()

i = 0
while (i < len(line)):
    if (line[i][0] != '-'):
        # do nothing
        cleanString = line[i].replace("\n","")
        cleanString = cleanString.replace("+","")
        cleanString = cleanString.replace(" ","")
        
        listOfWord.append(cleanString)
    i+=1
inString.close()

# START TIME
startTime = time.time()
problemSolver(listOfWord,listOfNode)
# print(problemSolver(listOfWord))

print(problemSolver(listOfWord))
displayWord(listOfWord)
displayAngka()
# HITUNG RUNNING TIME
runningTime = (time.time() - startTime)
print(runningTime)
