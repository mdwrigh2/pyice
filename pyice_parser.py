import yacc
import pyice_lexer

import sys

tokens = pyice_lexer.tokens

precedence = (
    ('nonassoc', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH', 'MOD'),
    ('right', 'UMINUS')
)

#def p_statement_01(t):
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

def p_statement_05(t):
    '''stm : WRITE exp SEMI'''

def p_statement_06(t):
    '''stm : lvalue ASSIGN exp SEMI'''

def p_expression(t):
    '''exp : INT
           | TRUE
           | FALSE
           | STRING
           | READ'''

def p_unary_expression(t):
    ''' exp : MINUS exp %prec UMINUS
            | QUEST exp'''

def p_procedure_call_expression(t):
    ''' exp : ID LPAREN RPAREN
            | ID LPAREN argument_list RPAREN'''

def p_argument_list(t):
    ''' argument_list : exp
                      | exp COMMA argument_list'''

def p_binary_expression(t):
    ''' exp : exp PLUS exp
            | exp MINUS exp
            | exp STAR exp
            | exp SLASH exp
            | exp MOD exp
            | exp EQ exp
            | exp NEQ exp
            | exp GT exp
            | exp LT exp
            | exp GE exp
            | exp LE exp'''

def p_expression_parens(t):
    ''' exp : LPAREN exp RPAREN'''

def p_lvalue(t):
    ''' lvalue : ID
               | lvalue LBRACK exp RBRACK'''

def p_typeid(t):
    ''' typeid : ID''' # just for semantics

def p_declist(t):
    '''declist : declistx
               | empty'''

def p_declistx(t):
    '''declistx : idlist COLON typeid
                | idlist COLON typeid COMMA declistx'''

def p_type(t):
    ''' type : TYPE ID EQ '''
def p_empty(t):
    'empty :'
    pass

def p_error(t):
    print "Syntax error around line %d" % t.lineno
    sys.exit()

yacc.yacc(debug=1)
