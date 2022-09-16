#Analizador lexico
#Jesus Garcia Hernandez     A01423730
import sys
import SymbolTable

#Variables
skippedCharacters = SymbolTable.skippedCharacters
separators = SymbolTable.separators
reservedWords = SymbolTable.reservedWords
readedTokens = []

def readFile():
    global file
    with open("Code.txt") as f:
        file = f.readlines() 

def analize():
    delimitedComment = False
    
    for line in file:
        currToken = ""
        for i in range(0, len(line)):
            if(line[i] == '/' and line[i+1] == '/'): #Skip lines with one-line comment
                break;
            elif(delimitedComment == False and line[i] == '/' and line[i+1] == '*'):  #Begginning of a multi-line comment
                delimitedComment = True
            elif(delimitedComment == True and line[i-1] == '*' and line[i] == '/'):  #End of multi-line comment
                delimitedComment = False
            elif(delimitedComment == False):        #Begin lexical check
                if(line[i] in skippedCharacters):   #Check for skipping tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    continue
                elif(line[i] in separators):     #Check for separators
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i])
                else:
                    currToken = currToken + line[i]

def printTokens():
    isAString = False

    for i in range(0, len(readedTokens)):
        if (readedTokens[i] == ('"' or "'")):
            isAString = not isAString
            print(readedTokens[i], "QUOTATION_MARK")
        elif((readedTokens[i] in separators) and isAString == False):   #Print separators
            print(readedTokens[i], separators[readedTokens[i]])
        elif((readedTokens[i] in reservedWords) and isAString == False):    #Print reserved words
            print(readedTokens[i], reservedWords[readedTokens[i]])
        elif(isAString == True):                                        #Print string literals
            print(readedTokens[i], "LineString")
        else:
            print(readedTokens[i], "ID")                                                   # All other characters are id's
            #raise Exception("Not recognized character", readedTokens[i])

# Driver code
readFile()
analize()
printTokens()