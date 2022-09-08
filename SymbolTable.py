skippedCharacters = [" ", "\t", "\n"]

delimiters = {
    "(": "OPENING_PARENTHESIS",
    ")": "CLOSING_PARENTHESIS",
    ":": "DOUBLE_DOT",
    "<": "OPENING_TYPE_BRACKET",
    ">": "CLOSING_TYPE_BRACKET",
    '"': "QUOTATION_MARK",
}

reservedWords = {
    "println": "PRINT_FUNCTION",
    "fun": "FUNCTION_DECLARATION",
    "main": "FUNCTION_TYPE",
}