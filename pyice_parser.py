import yacc
import pyice_lexer

tokens = pyice_lexer.tokens

#def p_statement(t):
    #'''stm : if 
           #| do
           #| fa
           #| BREAK SEMI
           #| EXIT SEMI'''
def p_statement_02(t):
    '''stm : RETURN SEMI'''

def p_statement_03(t):
    '''stm : exp SEMI'''

def p_statement_04(t):
    '''stm : SEMI'''

def p_expression(t):
    '''exp : INT'''

#def p_expression_02(t):


#def p_expression


def p_empty(t):
    'empty :'
    pass

def p_error(t):
    print "Syntax error around line %d" % t.lineno

yacc.yacc(debug=1)
