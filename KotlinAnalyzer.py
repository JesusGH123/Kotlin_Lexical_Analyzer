#Analizador lexico
#Jesus Garcia Hernandez     A01423730
import sys
import SymbolTable
import colorama
import re
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
            elif(line[i] == "#" and line[i+1] == "!"):
                readedTokens.append(line[i]+line[i+1])
                break
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
                elif(i+1 < len(line) and line[i]+line[i+1] in separators): #2 character tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i]+line[i+1])
                    skipTokens = 1
                elif(line[i] in separators and (currToken + line[i]) not in reservedWords): # character tokens
                    if(currToken != ""):
                        readedTokens.append(currToken)
                        currToken = ""
                    readedTokens.append(line[i])
                else:
                    currToken = currToken + line[i]

def classifyTokens():
    isAString = False
    isAnInterpolation = False

    for i in range(0, len(readedTokens)):
        if (readedTokens[i] == '"""' or readedTokens[i] == "'" or readedTokens[i] == '"'):
            isAString = not isAString
            print(readedTokens[i], separators[readedTokens[i]])
        elif(isAString and "${" in readedTokens[i]):
            isAnInterpolation = True
            print(readedTokens[i], "String interpolation")
        elif(isAString and "}" in readedTokens[i]):
            isAnInterpolation = False
            print(readedTokens[i], "String interpolation")
        elif(isAString and isAnInterpolation == False):       #Print strings
            print(readedTokens[i], "LineString")
        elif(isAString and isAnInterpolation):
            #tokenValidation(readedTokens[i])
            print(readedTokens[i], "String interpolation")
        elif((readedTokens[i] in separators) and isAString == False):  #Print separators
            print(readedTokens[i], separators[readedTokens[i]])
        elif((readedTokens[i] in reservedWords) and isAString == False):    #Print reserved words
            print(readedTokens[i], reservedWords[readedTokens[i]])
        else:
            literalValidation(readedTokens[i], False)

def literalValidation(token, secondLap):
    if(re.match(r'((^[1-9]+(\_*[0-9]*)*[0-9]$)|(^[0-9]$))', token)):
        print(token, "IntegerLiteral")
    elif(re.match(r'^[0-9]*\.?[0-9]+[fF]$', token)):
        print(token, "RealLiteral")
    elif(re.match(r'^[0-9]*\.?[0-9]+([eE][\+|\-]?[0-9]+)?$', token)):
        print(token, "RealLiteral")
    elif(re.match(r'((^(0[xX])[0-9a-fA-F](\_*[0-9a-fA-F]*)*[0-9a-fA-F]$)|(^(0[xX])[0-9a-fA-F])$)', token)):
        print(token, "HexLiteral")
    elif(re.match(r'((^(0[bB])[01](\_*[01]*)*[01]$)|(^(0[bB])[01])$)', token)):
        print(token, "BinLiteral")
    else:
        if(secondLap == False):
            tokenValidation(token)
        else:
            return False
        
def searchError(IncorrectToken):
    for line in range(0, len(file)):    #Search the error in the code
        if IncorrectToken in file[line]:
            return str(line+1)  

def tokenValidation(token):
    splitters = ['+','-','.']
    splittedToken = []
    currToken = ""

    for i in range(0, len(token)+1):
        if(i<len(token) and token[i] in splitters):
            splittedToken.append(currToken)
            splittedToken.append(token[i])
            currToken = ""
        elif(i == len(token)):
            splittedToken.append(currToken)
        else:
            currToken += token[i]
    
    for token in splittedToken:
        for character in token:         #Validate the token
            if(character not in alphabet and
                character not in reservedWords and
                character not in separators):
                print(Fore.RED + "ERROR: Non recognized character at line " + searchError(token) + Fore.WHITE)
                exit(-1)
        if(token in reservedWords):
            print(token, reservedWords[token])
        else:
            if(literalValidation(token, True) == False):
                print(token, "ID")

# Driver code
readFile()
analize()
classifyTokens()