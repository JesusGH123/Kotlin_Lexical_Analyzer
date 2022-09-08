#Analizador lexico
#Jesus Garcia Hernandez     A01423730
import sys
import SymbolTable

#Variables
skippedCharacters = SymbolTable.skippedCharacters
delimiters = SymbolTable.delimiters
reservedWords = SymbolTable.reservedWords
readedTokens = []

def readFile():
    global file
    with open(sys.argv[1]) as f:
        file = f.readlines()
    

def analize():
    for line in file:
        currToken = ""
        if(line.startswith("//") == False):  #Ignore one-line comments
            for i in range(0, len(line)-1):
                if(line[i] in skippedCharacters):   #Check for skipping tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    continue
                elif(line[i] in delimiters):     #Check for delimiters
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i])
                else:
                    currToken = currToken + line[i]
                    

def printTokens():
    for i in range(0, len(readedTokens)):
        if(readedTokens[i] in delimiters):
            print(readedTokens[i], delimiters[readedTokens[i]])
        elif(readedTokens[i] in reservedWords):
            print(readedTokens[i], reservedWords[readedTokens[i]])
        else:
            print("Not recognized character: ", readedTokens[i])

# Driver code
readFile()
analize()
printTokens()