#Analizador lexico
#Jesus Garcia Hernandez     A01423730
import sys
import SymbolTable
import colorama
from colorama import Fore

#Variables
skippedCharacters = SymbolTable.skippedCharacters
separators = SymbolTable.separators
reservedWords = SymbolTable.reservedWords
alphabet = SymbolTable.alphabet
readedTokens = []

def readFile():
    global file
    with open("Code.txt") as f:
        file = f.readlines() 

def analize():
    delimitedComment = False
    
    for line in file:
        currToken = ""
        skipTokens = 0
        for i in range(0, len(line)):
            if(line[i] == '/' and line[i+1] == '/'): #Skip lines with one-line comment
                break
            elif(delimitedComment == False and line[i] == '/' and line[i+1] == '*'):  #Begginning of a multi-line comment
                delimitedComment = True
            elif(delimitedComment == True and line[i-1] == '*' and line[i] == '/'):  #End of multi-line comment
                delimitedComment = False
            else:        #Begin lexical check
                if(line[i] in skippedCharacters):   #Check for skipping tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                elif(skipTokens > 0):
                    skipTokens = skipTokens - 1
                elif(i+2 < len(line) and line[i]+line[i+1]+line[i+2] in separators):    #3 character tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i]+line[i+1]+line[i+2])
                    skipTokens = 2
                elif(i+1 < len(line) and line[i]+line[i+1] in separators):
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i]+line[i+1])
                    skipTokens = 1
                elif(line[i] in separators and (currToken + line[i]) not in reservedWords):
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i])
                else:
                    currToken = currToken + line[i]

def classifyTokens():
    isAString = False

    for i in range(0, len(readedTokens)):
        if (readedTokens[i] == '"' or readedTokens[i] == "'" or readedTokens[i] == '"""'):
            isAString = not isAString
            print(readedTokens[i], separators[readedTokens[i]])
        elif(isAString == True):                             #Print strings
            print(readedTokens[i], "LineString")
        elif((readedTokens[i] in separators) and isAString == False):  #Print separators
            print(readedTokens[i], separators[readedTokens[i]])
        elif((readedTokens[i] in reservedWords) and isAString == False):    #Print reserved words
            print(readedTokens[i], reservedWords[readedTokens[i]])
        else:
            for character in readedTokens[i]:
                if(character not in alphabet):
                    print(Fore.RED + "ERROR: Non recognized character at line " + searchError(readedTokens[i]) + Fore.WHITE)
                    return
            print(readedTokens[i], "ID")

def searchError(IncorrectToken):
    for line in range(0, len(file)):
        if IncorrectToken in file[line]:
            return str(line+1)  

# Driver code
readFile()
analize()
classifyTokens()