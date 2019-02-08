# Hello! This is one of the first hard assignment I made studying Python 3. I record this program on 08.02.2019 at the age of 16
# Program: theSpiral
# Purpose: create an n*n grid using matrix that way that numbers are printing inward in spiral way
# Output: itarate the matrix
# The level of syntax knowledge: minimal
# Time: 3 hours to make 
# Result: fullfilled using the knowledge obtained from the basic python course

n = int(input("Please enter the size of the desireable matrix: ")) # Input any desirable integer number 
kekList = [[0] * n for i in range (n)]  # Generate a matrix and fill it in with zeros for furute manipulations
c = 0 # Counter; represents the next number in range (1, n*n + 1)
yes = 0 # Argument; decreases the gap between the ranges of the matrix during the moves
count = 1 # Counter; I noticed that the amount of moves right-down-left-up can be determined:
for x in range (1, n): #... this way
    count+= 2 # A funny thing I noticed is that to determine the number of moves visually all you have to do is to look at the bottom right number of the final matrix.  
for yes in range (0, count // 4 + 1): # This way loop checks the amount of times it has to run before the start of the loop itself. I wonder if while loop will be more efficient, but I have to use c counter for the logic of the program, so yeah :\
    for x in range (yes, n - yes): # Move right. Alright I can see right here that the code can and must be optimized... Basically, I have to many if statement. Obviously I should have used elif statements but that would require the rewriting the hole program which it is too mendokse (Jap.)
        c += 1 # Increase the counter
        if c > n**2:
            break # Break from the cycle to avoid overwork 
        else:
            kekList[yes][x] = c # The main logical statement
    yes += 1
    if c > n ** 2:
        break
    for x in range (yes, n + 1 - yes): # Пара 2 вниз
        c += 1
        if c > n ** 2:
            break
        else: kekList [x][n - yes] = c
    if c > n ** 2:
        break
    for x in range (n-yes - 1, yes-2, -1): # Пара 3 влево
        c += 1
        if c > n ** 2:
            break
        else: kekList [n - yes][x] = c
    if c > n ** 2:
        break
    for x in range (n - yes - 1, yes-1, -1): # Пара 4 вверх
        c += 1
        if c > n ** 2:
            break
        else: kekList [x][yes - 1] = c
    if c > n ** 2:
        break
        
for x in kekList: # Print 
    for y in x:
        print (y, end = "\t")
    print()
