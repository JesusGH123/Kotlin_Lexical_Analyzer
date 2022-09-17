skippedCharacters = [" ", "\t", "\n", "\r\n", "\r"]

separators = {
    "#!": "SheBangLine",

    #Separators and operations
    "...": "RESERVED", ".": "DOT", ",": "COMMA",
    "(": "LPAREN", ")": "RPAREN", "[": "LSQUARE", "]": "RSQUARE", "{": "LCURL", "}": "RCURL",
    "*": "MULT", "%": "MOD", "/": "DIV", "+": "ADD", "-": "SUB",
    "++": "INCR", "--": "DECR", "&&": "CONJ", "||": "DISJ", "!": "EXCL_WS",
    ":": "COLON", ";": "SEMICOLON",
    "=": "ASSIGNMENT", "+=": "ADD_ASSIGNMENT", "-=": "SUB_ASSIGNMENT", "*=": "MULT_ASSIGNMENT", "/=": "DIV_ASSIGNMENT", "%=": "MOD_ASSIGNMENT",
    "->": "ARROW", "=>": "DOUBLE_ARROW", "..": "RANGE", "::": "COLONCOLON", ";;": "DOUBLE_SEMICOLON",
    "#": "HASH", "@": "AT_NO_WS", "?": "QUEST_WS",
    "<": "LANGLE", ">": "RANGLE", "<=": "LE", ">=": "GE",
    "!=": "EXCL_EQ", "EXCL_EQEQ": "!==", "as?": "AS_SAFE", "==": "EQEQ", "===": "EQEQEQ",
    "'": "SINGLE_QUOTE", '"': "QUOTE_OPEN",'"""': "TRIPLE_QUOTE_OPEN", "&": "AMP", "${": "LineExprStart",

    "0": "DecDigit", "1": "DecDigit", "2": "DecDigit", "3": "DecDigit", "4": "DecDigit", "5": "DecDigit", "6": "DecDigit", "7": "DecDigit", "8": "DecDigit", "9": "DecDigit",
}

reservedWords = {
    #Keywords
    "return@": "RETURN_AT", "continue@": "CONTINUE_AT", "break@": "BREAK_AT", "this@": "THIS_AT", "super@": "SUPER_AT",
    "file": "FILE", "field": "FIELD", "property": "PROPERTY", "get": "GET", "set": "SET", "receiver": "RECEIVER",
    "param": "PARAM", "setparam": "SETPARAM", "delegate": "DELEGATE",
    "package": "PACKAGE", "import": "IMPORT", "class": "CLASS", "interface": "INTERFACE", "fun": "FUN", "object": "OBJECT",
    "val": "VAL", "var": "VAR", "typealias": "TYPE_ALIAS", "constructor": "CONSTRUCTOR", "by": "BY", "companion": "COMPANION",
    "init": "INIT", "this": "THIS", "super": "SUPER", "typeof": "TYPEOF", "where": "WHERE", "if": "IF", "else": "ELSE", "when": "WHEN",
    "try": "TRY", "catch": "CATCH", "finally": "FINALLY", "for": "FOR", "do": "DO", "while": "WHILE", "throw": "THROW", "return": "RETURN", "continue": "CONTINUE", "break": "BREAK",
    "as": "AS", "is": "IS", "in": "IN", "!is": "NOT_IS", "!in": "NOT_IN", "out": "OUT", "dynamic": "dynamic", "IT": "it",
    #Lexical modifiers
    "public": "PUBLIC", "private": "PRIVATE", "protected": "PROTECTED", "internal": "INTERNAL", "enum": "ENUM", "sealed": "SEALED", "annotation": "ANNOTATION", "data": "DATA", "inner": "INNER",
    "value": "VALUE", "tailrec": "TAILREC", "operator": "OPERATOR", "inline": "INLINE", "infix": "INFIX", "external": "EXTERNAL", "suspend": "SUSPEND", "override": "OVERRIDE", "abstract": "ABSTRACT",
    "final": "FINAL", "open": "OPEN", "const": "CONST", "lateinit": "LATEINIT", "vararg": "VARARG", "noinline": "NOINLINE", "crossonline": "CROSSINLINE", "reified": "REIFIED", "expect": "EXPECT", "actual": "ACTUAL",
    #Section: Literals
    "_": "Separator", "e": "Exponent", "E": "Exponent",
    "true": "BooleanLiteral", "false": "BooleanLiteral", "null": "NullLiteral", "\\": "CharacterLiteral", "$": "FieldIdentifier",

    #Extras
    "Array": "ARRAY", "ListOf": "LIST_TYPE", "MutableList": "mutableListOf", "SET_TYPE": "setOf",  "MAP_TYPE": "mapOf", "MUTABLE_MAP": "mutableMapOf",
    "String": "DATA_TYPE", "Float": "DATA_TYPE", "Int": "DATA_TYPE", "Char": "DATA_TYPE", "Double": "DATA_TYPE", "Boolean": "DATA_TYPE", "Byte": "DATA_TYPE", "Short": "DATA_TYPE", "Long": "DATA_TYPE",
}

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']