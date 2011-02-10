import yacc
import pyice_lexer

import sys

class ParseError(Exception):
    def __init__(self, lineno, token):
        self.lineno = lineno
        self.token = token
    def __str__(self):
        return repr(self.token)

tokens = pyice_lexer.tokens

precedence = (
    ('nonassoc', 'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'STAR', 'SLASH', 'MOD'),
    ('right', 'UMINUS')
)

start = 'program'

debug = 1


def p_program(t):
    ''' program : begins
                | begins stms'''

def p_begins(t):
    ''' begins : var begins
               | type begins
               | forward begins
               | proc begins
               | empty'''

def p_statements(t):
    '''stms : stm stms
            | stm'''

def p_statement_01(t):
    '''stm : if 
           | do
           | fa
           | BREAK SEMI
           | EXIT SEMI'''

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

#Need to add the { '[]' exp '->' stms }
def p_if_01(t):
    '''if : IF exp ARROW stms FI
          | IF exp ARROW stms ifboxes FI'''

def p_ifboxes(t):
    '''ifboxes : BOX exp ARROW stms ifboxes
               | empty '''

def p_if_02(t):
    '''if : IF exp ARROW stms select'''

def p_select(t):
    ''' select : BOX exp ARROW stms select
                | BOX ELSE ARROW stms FI'''

def p_do(t):
    '''do : DO exp ARROW OD
          | DO exp ARROW stms OD'''

def p_fa(t):
    '''fa : FA ID ASSIGN exp TO exp ARROW AF
          | FA ID ASSIGN exp TO exp ARROW stms AF'''

def p_proc_01(t):
    '''proc : PROC ID LPAREN declist RPAREN typevars END'''

def p_proc_02(t):
    '''proc : PROC ID LPAREN declist RPAREN typevars stms END'''

def p_proc_03(t): 
    '''proc : PROC ID LPAREN declist RPAREN COLON typeid typevars END'''

def p_proc_04(t):
    '''proc : PROC ID LPAREN declist RPAREN COLON typeid typevars stms END'''


def p_typevars(t):
    ''' typevars : var typevars
                 | type typevars
                 | empty'''

def p_idlist(t):
    '''idlist : ID
              | ID COMMA idlist'''

def p_var(t):
    ''' var : VAR varlist SEMI'''

def p_varlist(t):
    '''varlist : idlist COLON typeid
               | idlist COLON typeid COMMA varlist'''

def p_varlist_arrays(t):
    ''' varlist : idlist COLON typeid intarrays
                | idlist COLON typeid intarrays COMMA varlist'''

def p_arrays(t):
    ''' intarrays : LBRACK INT RBRACK
                  | LBRACK INT RBRACK intarrays'''

def p_forward(t):
    '''forward : FORWARD ID LPAREN declist RPAREN SEMI
               | FORWARD ID LPAREN declist RPAREN COLON typeid SEMI'''


def p_exp_array(t):
    ''' exparray : LBRACK exp RBRACK
                  | LBRACK exp RBRACK exparray '''

def p_expression(t):
    '''exp : INT
           | TRUE
           | FALSE
           | STRING
           | READ'''
    #t[0] = t[1]

def p_expression_02(t):
    ''' exp : ID'''

def p_expression_array(t):
    ''' exp : ID exparray'''


def p_unary_expression(t):
    ''' exp : MINUS exp %prec UMINUS
            | QUEST exp'''
    #if t[1] == '-':
        #t[0] = -t[2]
    #else:
        #if t[2]:
            #t[0] = 1
        #else:
            #t[0] = 0

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
    #if t[2] == '+':
        #t[0] = t[1] + t[3]

def p_expression_write(t):
    ''' exp : WRITE exp
            | WRITES exp'''


def p_expression_parens(t):
    ''' exp : LPAREN exp RPAREN'''

def p_lvalue(t):
    ''' lvalue : ID
               | ID exparray'''

def p_typeid(t):
    ''' typeid : ID''' # just for semantics

def p_declist(t):
    '''declist : declistx
               | empty'''

def p_declistx(t):
    '''declistx : idlist COLON typeid
                | idlist COLON typeid COMMA declistx'''

def p_type(t):
    ''' type : TYPE ID EQ typeid SEMI
             | TYPE ID EQ typeid intarrays SEMI'''


def p_empty(t):
    'empty :'
    pass

def p_error(t):
    raise ParseError(t.lineno, t.value)

yacc.yacc()
