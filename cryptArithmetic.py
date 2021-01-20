
import time



#MENGECEK KENUIKAN KARAKTER
def isUnique(n, p) :
    if (n == 0) :
        return True

    number = []
    count = 0
    while (n >= 1) :
        number.insert(n%10)
        count += 1
        n /= 10

    return (count == number.len())


#MAIN PROGRAM

# START TIME
startTime = time.time()

# KAMUS

# open file
inString = open("input.txt", "r")
outString = open("output.txt", "w")


# HITUNG RUNNING TIME
runningTime = (time.time() - startTime)
