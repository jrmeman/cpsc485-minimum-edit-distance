"""
CPSC 485 - Minimum Edit Distance Program

Name: Justin Meman
CWID: 5781

Language used: Python (vanilla)
Program created and ran on: Visual Studio Code
I suggest running the program on Visual Studio Code as I have not tested the file on any other IDE.

This program asks for user to input two strings and calculates the minimum edit distance between the two.
Outputs an edit distance matrix, the minimum edit distance, and the appropriate alignment of the given words.
"""

# Edit Distance function does all minimum distance calculation and alignment
def EditDistance(word1, word2):
    rows = len(word1)+1
    cols = len(word2)+1
    # Creates a zeroed out matrix for edit distance
    matrix = [[0 for x in range(cols)] for x in range(rows)]

    # Creates a zeroed out matrix for directions
    # 5 = substition, 6 = deletion, 7 = insertion 
    matrix2 = [[0 for x in range(cols)] for x in range(rows)]

    # Fills out first column of matrix 1 (skipping the first row) with 1 to (len(word1) - 1)
    for i in range(1, rows):
        matrix[i][0] = i

    # Fills out first row of matrix 1 (skipping the first column) with 1 to (len(word2) - 1)
    for i in range(1, cols):
        matrix[0][i] = i
   
    # Nested for loop that populates both matrices [Matrix 1 for edit distance, Matrix 2 for directions]
    for y in range(1, cols):
        for x in range(1, rows):
            # if else case accounts for same letter comparison
            if word1[x-1] == word2[y-1]:
                cost = 0
            else:
                cost = 1
            
            # Deletion
            de = matrix[x-1][y] + 1
            # Insertion
            ins = matrix[x][y-1] + 1
            # Substitution
            sub = matrix[x-1][y-1] + cost

            # Dictionary to store for direction matrix
            data = {6 : de, 7 : ins, 5 : sub}
            
            # If letters are same, it's equivalent to getting value from subsititon slot [Fill matrix 2 slot with 'sub']
            if word1[x-1] == word2[y-1]:
                matrix2[x][y] = 5
            
            # if case where length of words are currently same, but two diff min values
            if len(word1[:x]) == len(word2[:y]):
                # if the minimum is the sub box, fill it with sub value
                if min(data, key=data.get) == 5:
                    matrix2[x][y] = 5
                # else fill it with ins/del value (depending on which is smaller)
                else:
                    matrix2[x][y] = min(data, key=data.get)
            
            # if case where two diff min values (prefer ins/del over sub)
            else:   
                if de == sub:
                    matrix2[x][y] = 6
                if ins == sub:
                    matrix2[x][y] = 7
                # final else case where box is just the minimum of the 3 values
                else:
                    matrix2[x][y] = min(data, key=data.get)
            
            # Traverses the full matrix and fills out the elements column by column
            matrix[x][y] = min(de, ins, sub)            

    # Prints completed matrix
    for i in range(rows):
        print(matrix[i])
    
    # Returns minimum edit distance of both words
    print("Minimum edit distance: " + str(matrix[x][y]))

    # Alignment Time
    # Initialize 2 empty strings
    alignment1 = ""
    alignment2 = ""

    # While loop continues until Matrix 2 reaches [0][0]
    while x != 0 and y != 0:
        # If current box is insertion, insert last char of word2 to alignment2, insert "_" to alignment1, decrement column
        if matrix2[x][y] == 7:
            alignment2 = alignment2 + word2[y-1]
            alignment1 = alignment1 + "_"
            y = y - 1
        # If current box is deletion, insert last char of word1 to alignment1, insert "_" to alignment2, decrement row
        elif matrix2[x][y] == 6:
            alignment1 = alignment1 + word1[x-1]
            alignment2 = alignment2 + "_"
            x = x - 1
        # If current box is substitution, insert last char of both words to both alignments respectively, decrement both row and column
        elif matrix2[x][y] == 5:
            alignment1 = alignment1 + word1[x-1]
            alignment2 = alignment2 + word2[y-1]
            x = x - 1
            y = y - 1

    # Print alignment of both words in reverse
    print("\nAlignment: ")
    print(alignment1[::-1])
    print(alignment2[::-1])

# Main portion of code where user inputs words and is used for function call to return answer
word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
EditDistance(word1, word2)