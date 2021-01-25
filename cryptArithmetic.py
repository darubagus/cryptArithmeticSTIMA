
import time


# listOfNode = [{letter, corresponding value}]
use = [0 for i in range(10)]

listOfWord = []

# MENGECEK APAKAH
# def isValid(listOfNode, count, word1, word2, word3):
#     val1 = 0
#     val2 = 0
#     val3 = 0
#     # j,i

#     m = 1
#     i = word1.len()-1
#     while (i>=0):
#         ch = word1[i]
#         for j in range(count) :
#             if (listOfNode[j][0] == ch):
#                 break
#         val2 += m * listOfNode[j][1]
#         m *= 10
#         i-=1

#     m = 1
#     i = word2.len()-1
#     while (i>=0):
#         ch = word2[i]
#         for j in range(count) :
#             if (listOfNode[j][0] == ch):
#                 break
#         val2 += m * listOfNode[j][1]
#         m *= 10
#         i-=1

#     m = 1
#     i = word3.len()-1
#     while (i>=0):
#         ch = word3[i]
#         for j in range(count) :
#             if (listOfNode[j][0] == ch):
#                 break
#         val2 += m * listOfNode[j][1]
#         m *= 10
#         i-=1

#     if (val3 == (val1+val2)):
#         return True
#     else :
#         return False

def isValid(listOfNode, count, listOfWord) :
    val = [0 for i in range(len(listOfWord)-1)]
    temp = 0
    totalVal=0

    for z in range(len(listOfWord)-1):
        m = 1
        i = len(listOfWord[z])-1
        while (i >= 0) :
            char = listOfWord[z][i]
            for j in range(count) : 
                temp = j
                if (listOfNode[j][0] == char) :
                    break
            val[z] += m * listOfNode[temp][1]
            m *= 10
            i-=1
    
    # buat ngecek hasil
    for i in range(len(listOfWord)-2) :
        totalVal += val[i]
    
    if (totalVal == val[len(listOfWord)-1]) :
        return True
    else:
        return False


def Permutate(count, listOfNode, n, listOfWord) :
    if (n == count-1): #Basis
        for i in range(10):
            if (use[i] == 0):
                listOfNode[n][1] = i
                if (isValid(listOfNode,count,listOfWord)) :
                    print("Solusi ditemukan\n")
                    # for j in range(count) :
                    #     print(listOfNode[j][0]+" = "+listOfNode[j][1]+"\n")
                    # print letter and its corresponding value
                    return True
        return False
    else:
        for i in range(10):
            if (use[i]==0):
                listOfNode[n][1] = i
                use[i] = 1
                if (Permutate(count,listOfNode, n+1,listOfWord)):
                    return True
                use[i] = 0
        return False # only for precaution

def problemSolver(listofWord):
    char = 0
    

#MAIN PROGRAM


# for testing purpose



# START TIME
startTime = time.time()

# KAMUS

# open file
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
    
outString = open("output.txt", "w")


# HITUNG RUNNING TIME
runningTime = (time.time() - startTime)
