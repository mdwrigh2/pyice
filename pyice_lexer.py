import lex
import re
import sys

# ----------------------------------------
# Reserved words
# They are also tokens
# ----------------------------------------

reserved = (
    'IF',
    'FI',
    'ELSE',
    'DO',
    'OD',
    'FA',
    'AF',
    'TO',
    'PROC',
    'END',
    'RETURN',
    'FORWARD',
    'VAR',
    'TYPE',
    'BREAK',
    'EXIT',
    'TRUE',
    'FALSE',
    'WRITE',
    'WRITES',
    'READ'
)

# ----------------------------------------
# Tokens
# ----------------------------------------

tokens = reserved + (
    'BOX',
    'ARROW',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'COLON',
    'SEMI',
    'ASSIGN',
    'QUEST',
    'COMMA',
    'PLUS',
    'MINUS',
    'STAR',
    'SLASH',
    'MOD',
    'EQ',
    'NEQ',
    'GT',
    'LT',
    'GE',
    'LE',
    'INT',
    'STRING',
    'ID'
)

# ----------------------------------------
# Create a map with each of the reserved words
# mapping to its type
# ----------------------------------------

reserved_words = { }

for word in reserved:
    reserved_words[word.lower()] = word


# ----------------------------------------
# How to identify tokens
# ----------------------------------------

t_BOX       = r'\[\]'
t_ARROW     = r'->'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACK    = r'\['
t_RBRACK    = r'\]'
t_COLON     = r':'
t_SEMI      = r';'
t_ASSIGN    = r':='
t_QUEST     = r'\?'
t_COMMA     = r','
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_STAR      = r'\*'
t_SLASH     = r'/'
t_MOD       = r'%'
t_EQ        = r'='
t_NEQ       = r'!='
t_GT        = r'>'
t_LT        = r'<'
t_GE        = r'>='
t_LE        = r'<='



# ----------------------------------------
# Handle the more complex tokens
# ----------------------------------------

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    if reserved_words.has_key(t.value):
        t.type = reserved_words[t.value]
    return t

def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'("[^"\n]*")|(\'[^\'\n]*\')' # match either double or single quoted string literals
    return t

# ----------------------------------------
# Handle ignored (whitespace) tokens 
# ----------------------------------------
def t_WHITESPACE(t):
    r'[ \t\r\f\v\n]+'
    t.lexer.lineno += t.value.count("\n")
    pass

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# I need to check this, because this may be eating too many new lines
# I think it should be okay though
# another worry is that the new lines aren't being counted properly.
# I'll have to test this in my program output
def t_COMMENT(t):
    r'\#[^\n]*'
    pass


# ----------------------------------------
# Handle Errors
# ----------------------------------------

def t_error(t):
    print "On line %d: " % (t.lineno,) + "",
    if t.value[0] == '"' or t.value[0] == "'":
        print "unterminated string"
    else:
        print "parse error near %s" % t.value
    sys.exit(1)
    
# Give it a main function to test the lexer

def test_lex():
    import sys
    file = open(sys.argv[1])
    lines = file.readlines()
    file.close()
    prog = "".join(lines)
    lex.input(prog)
    while True:
        token = lex.token()
        if not token: break
        print "(%s, '%s', %d)" % (token.type, token.value, token.lineno)

lex.lex()

if __name__ == '__main__':
    test_lex()
