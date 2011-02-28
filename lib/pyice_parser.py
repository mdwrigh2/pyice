import yacc
import pyice_lexer

import symbol_table

import sys

from nodes import *

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


variables = symbol_table.SymbolTable()
functions = symbol_table.SymbolTable()
types     = symbol_table.SymbolTable([{'int': ('int', []), 'bool': ('bool',[]), 'string': ('string', [])},{}])

class Breaks(object):
    def __init__(self):
        self.breaks = 0

    def inc(self):
        self.breaks += 1

    def dec(self):
        self.breaks -= 1
    
    def can_break(self):
        if self.breaks < 1:
            return False
        else:
            return True



breaks = Breaks()

def p_program(t):
    ''' program : begins
                | begins stms'''
    # Null statement, everything happens in the actions
    pass

def p_begins(t):
    ''' begins : var begins
               | type begins
               | forward begins
               | proc begins
               | empty'''
    # Null statement, everything happens in the actions
    pass

def p_statements(t):
    '''stms : stm stms'''
    tmp = t[2]
    tmp.append(t[1])
    t[0] = tmp


def p_statements_initial(t):
    '''stms : stm'''
    # Null statement, everything happens in the actions
    t[0] = [t[1]]

def p_statement_01(t):
    '''stm : if 
           | do
           | fa'''
    # Null statment, everything happens in the actions themselves
    t[0] = t[1]

def p_statement_break(t):
    '''stm : BREAK SEMI'''
    if not breaks.can_break():
        raise TypeError(t.lineno(1), 'break statement outside of appropriate loop')
    else:
        #break_stmt -= 1
        pass
    BreakNode()

def p_statement_exit(t):
    '''stm : EXIT SEMI'''
    ExitNode()

def p_statement_02(t):
    '''stm : RETURN SEMI'''
    ReturnNode()

def p_statement_03(t):
    '''stm : exp SEMI'''
    t[0] = t[1]

def p_statement_04(t):
    '''stm : SEMI'''
    # Null statement
    pass

def p_statement_05(t):
    '''stm : WRITE exp SEMI
           | WRITES exp SEMI'''
    t[0] = WriteNode(t[1], t[2], t.lineno(1))

def p_statement_06(t):
    '''stm : lvalue ASSIGN exp SEMI'''
    t[0] = AssignNode(t[1], t[3], t.lineno(2))


def p_if_01(t):
    '''if : IF exp ARROW stms FI'''
    t[0] = IfNode(t[2], t[4], lineno = t.lineno(0))

def p_if_with_boxes(t):
    '''if : IF exp ARROW stms ifboxes FI'''
    t[0] = IfNode(t[2],t[4], t[5], lineno = t.lineno(0))


def p_ifboxes(t):
    '''ifboxes : BOX exp ARROW stms ifboxes'''
    tmp = [IfNode(t[2],t[4], lineno = t.lineno(0))]
    tmp.extend(t[5])
    t[0] = tmp
               
def p_ifboxes_empty(t):
    '''ifboxes : empty '''
    t[0] = []

def p_if_02(t):
    '''if : IF exp ARROW stms select'''
    tmp_select = t[5]
    tmp = tmp_select.pop()
    t[0] = IfNode(t[2], t[4], tmp_select, tmp, t.lineno(0))


def p_select(t):
    ''' select : BOX exp ARROW stms select'''
    tmp = [IfNode(t[2], t[4], lineno = t.lineno(1))]
    tmp.extend(t[5])
    t[0] = tmp


def p_select_else(t):
    ''' select : BOX ELSE ARROW stms FI'''
    t[0] = t[4]
    

def p_do(t):
    '''do : DO break_push exp ARROW OD'''
    t[0] = DoNode(t[3], NullNode(), t.lineno(1))
    breaks.dec()

def p_do_stmts(t):
    '''do : DO break_push exp ARROW stms OD'''
    t[0] = DoNode(t[3], t[4], t.lineno(1))
    breaks.dec()

def p_fa(t):
    '''fa : FA push_table fa_init ARROW AF'''
    t[0] = ForNode(t[3][0], t[3][1], t[3][2], lineno = t.lineno(0))
    breaks.dec()
    variables.pop()
    types.pop()

def p_fa_initial(t):
    '''fa_init : ID ASSIGN exp TO exp'''
    t[0] = [t[1], t[3], t[5]]
    var = VarNode(('int', []), t[1], t[3], is_writeable = False)
    variables.insert(t[1], var)
    breaks.inc()

def p_fa_stmts(t):
    '''fa : FA push_table fa_init ARROW stms AF'''
    t[0] = ForNode(t[3][0], t[3][1], t[3][2], t[5], t.lineno(0))
    breaks.dec()
    variables.pop()
    types.pop()

def p_proc_05(t):
    '''proc : PROC push_table proc_center typevars END'''
    if isinstance(t[3][2], NullNode):
        type = ()
    else:
        try:
            type = types.lookup_defaults(t[3][2])
        except symbol_table.SymbolLookupError,e:
            raise TypeError(t.lineno(1),str(e))
    proc = ProcNode(t[3][0], t[3][1], type, t[4], NullNode(), t.lineno(1)) 
    try:
        functions.insert_func(t[3][0], proc)
    except symbol_table.ProcInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    variables.pop()
    types.pop()
    t[0] = proc

def p_proc_06(t):
    '''proc : PROC push_table proc_center typevars stms END'''
    variables.pop()
    types.pop()
    if isinstance(t[3][2], NullNode):
        type = ()
    else:
        try:
            type = types.lookup(t[3][2])
        except symbol_table.SymbolLookupError,e:
            raise TypeError(t.lineno(1),str(e))
    try:
        proc = ProcNode(t[3][0], t[3][1], type, t[4], t[5], t.lineno(1)) 
        functions.insert_func(t[3][0], proc)
    except symbol_table.ProcInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = proc


def p_proc_no_ret(t):
    '''proc_center : ID LPAREN declist RPAREN'''
    proc = ProcNode(t[1], t[3], (), None, None, t.lineno(1))
    try:
        functions.insert_func(t[1], proc)
    except symbol_table.ProcInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = [t[1], t[3], NullNode()]

def p_proc_ret(t):
    '''proc_center : ID LPAREN declist RPAREN COLON typeid'''
    type = types.lookup(t[6])
    proc = ProcNode(t[1], t[3], type, None, None, t.lineno(1))
    try:
        functions.insert_func(t[1], proc)
        variables.insert(t[1], VarNode(type, t[1]))
    except symbol_table.SymbolInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = [t[1], t[3], t[6]]


def p_typevars(t):
    ''' typevars : var typevars
                 | type typevars
                 | empty'''
    # Null statement, everything happens in the vars and types themselves
    pass

def p_idlist(t):
    '''idlist : ID '''
    t[0] = [t[1]]

def p_idlist_expansion(t):
    '''idlist : ID COMMA idlist'''
    tmp = [t[1]]
    tmp.extend(t[3])
    t[0] = tmp

def p_var(t):
    ''' var : VAR varlist SEMI'''
    # Null statement. Everything happens in varlist
    pass

def p_varlist(t):
    '''varlist : idlist COLON typeid
               | idlist COLON typeid COMMA varlist'''
    type = types.lookup(t[3])
    for var in t[1]:
        try:
            variables.insert(var, VarNode(type, var))
        except symbol_table.SymbolInsertionError,e:
            raise TypeError(t.lineno(2), str(e))
    

def p_varlist_arrays(t):
    ''' varlist : idlist COLON typeid intarrays
                | idlist COLON typeid intarrays COMMA varlist'''
    type = types.lookup(t[3])
    tmp = t[4]
    tmp.extend(type[1])
    new_type = (type[0], tmp)
    for var in t[1]:
        variables.insert(var, VarNode(new_type))


def p_arrays(t):
    ''' intarrays : LBRACK INT RBRACK '''
    t[0] = [t[2]]

def p_arrays_expansion(t):
    ''' intarrays : LBRACK INT RBRACK intarrays'''
    tmp = [t[2]]
    tmp.extend(t[4])
    t[0] = tmp

def p_forward(t):
    '''forward : FORWARD push_table ID LPAREN declist_forward RPAREN SEMI'''
    proc = ProcNode(t[3], t[5], (), None, None, t.lineno(1))
    try:
        functions.insert_forward(t[3], proc)
    except symbol_table.SymbolInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = proc
    variables.pop()
    types.pop()

def p_forward_return_type(t):
    '''forward : FORWARD push_table ID LPAREN declist_forward RPAREN COLON typeid SEMI'''
    variables.pop()
    types.pop()
    type = types.lookup_defaults(t[8])
    proc = ProcNode(t[3], t[5], type, None, None, t.lineno(1))
    try:
        functions.insert_forward(t[3], proc)
    except symbol_table.SymbolInsertionError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = proc


def p_exp_array(t):
    ''' exparray : LBRACK exp RBRACK '''
    if t[2].type == ('int', []):
        t[0] = [1]
        # I'm ignoring the expressions values for now
    else:
        raise TypeError(t.lineno(0), t[1])

def p_exp_array_expansion(t):
    ''' exparray : LBRACK exp RBRACK exparray '''
    if t[2].type == ('int', []):
        tmp = [1]
        tmp.extend(t[4])
        t[0] = tmp
        # I'm ignoring the expressions values for now
    else:
        raise TypeError(t.lineno(0), t[1])


def p_expression_int(t):
    '''exp : INT '''
    t[0] = LitNode(t[1], ('int', []), t.lineno(1))

def p_expression_bool(t):
    ''' exp : TRUE
            | FALSE '''
    t[0] = LitNode(t[1], ('bool', []), t.lineno(1))

def p_expression_string(t):
    ''' exp : STRING'''
    t[0] = LitNode(t[1], ('string', []), t.lineno(0))

def p_expression_read(t):
    ''' exp : READ'''
    t[0] = ReadNode(t.lineno(1))


def p_expression_02(t):
    ''' exp : ID'''
    t[0] = variables.lookup(t[1])
    

def p_expression_array(t):
    ''' exp : ID exparray'''
    tmp = variables.lookup(t[1])
    t[0] = ArrayNode(tmp, t[2], t.lineno(1))



def p_unary_expression(t):
    ''' exp : MINUS exp %prec UMINUS
            | QUEST exp %prec UMINUS'''
    t[0] = UnaryOpNode(t[1], t[2], t.lineno(1))

def p_procedure_call_expression(t):
    ''' exp : ID LPAREN RPAREN'''
    try:
        proc = functions.lookup(t[1])
    except symbol_table.SymbolLookupError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = CallNode(proc, ArgNode(t.lineno(1)), t.lineno(1))

def p_procedure_call_with_args_expression(t):
    '''exp : ID LPAREN argument_list RPAREN'''
    try:
        proc = functions.lookup(t[1])
    except symbol_table.SymbolLookupError,e:
        raise TypeError(t.lineno(1), str(e))
    t[0] = CallNode(proc, t[3], t.lineno(0))

def p_argument_list(t):
    ''' argument_list : exp '''
    args = ArgNode(t.lineno(1))
    args.append(t[1])
    t[0] = args

 
def p_argument_list_expansion(t):
    ''' argument_list : exp COMMA argument_list'''
    args = t[3]
    args.append(t[1])
    t[0] = args


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
    t[0] = BinOpNode(t[2], t[1], t[3], t.lineno(2))
    

def p_expression_write(t):
    ''' exp : WRITE exp
            | WRITES exp'''
    t[0] = WriteNode(t[1], t[2], t.lineno(1))


def p_expression_parens(t):
    ''' exp : LPAREN exp RPAREN'''
    t[0] = t[2]

def p_lvalue(t):
    ''' lvalue : ID '''
    try:
        t[0] = variables.lookup(t[1])
    except symbol_table.SymbolLookupError, e:
        raise TypeError(t.lineno(1), str(e))



def p_lvalue_arr(t):
    ''' lvalue : ID exparray'''
    t[0] = ArrayNode(variables.lookup(t[1]), t[2], t.lineno(0))

def p_typeid(t):
    ''' typeid : ID''' # just for semantics
    t[0] = t[1]

def p_declist(t):
    '''declist : declistx'''
    t[0] = t[1]

def p_declist_empty(t):
    '''declist : empty'''
    t[0] = DecNode(t.lineno(0))

def p_declistx(t):
    '''declistx : idlist COLON typeid'''
    dec = DecNode(t.lineno(3))
    for i in t[1]:
        var = VarNode(types.lookup(t[3]),i)
        variables.insert(i, var)
        dec.append(var)

    t[0] = dec


def p_declistx_extension(t):
    '''declistx : idlist COLON typeid COMMA declistx'''
    dec = t[5]
    for i in t[1]:
        var = VarNode(types.lookup(t[3]),i)
        variables.insert(i, var)
        dec.append(var)
    t[0] = dec

def p_declist_forward(t):
    '''declist_forward : declistx_forward'''
    t[0] = t[1]

def p_declist_forward_empty(t):
    '''declist_forward : empty'''
    t[0] = DecNode(t.lineno(1))

def p_declistx_forward(t):
    '''declistx_forward : idlist COLON typeid'''
    dec = DecNode(t.lineno(3))
    for i in t[1]:
        var = VarNode(types.lookup(t[3]),i)
        dec.append(var)

    t[0] = dec


def p_declistx_forward_extension(t):
    '''declistx_forward : idlist COLON typeid COMMA declistx_forward'''
    dec = t[5]
    for i in t[1]:
        var = VarNode(types.lookup(t[3]),i)
        dec.append(var)
    t[0] = dec

def p_type(t):
    ''' type : TYPE ID EQ typeid SEMI'''
    try:
        types.insert(t[2], types.lookup(t[4]))
    except symbol_table.SymbolInsertionError,e:
        raise TypeError(t.lineno(1), str(e))

def p_type_arrays(t):
    ''' type : TYPE ID EQ typeid intarrays SEMI'''
    tmp = t[5]
    original_type = types.lookup(t[4])
    tmp.extend(original_type[1])
    types.insert(t[2], (original_type[0], tmp))

def p_empty(t):
    '''empty :'''
    pass

def p_push_table(t):
    '''push_table : '''
    variables.push()
    types.push()

def p_break_push(t):
    '''break_push : '''
    breaks.inc()

def p_error(t):
    if not t:
        raise ParseError(-1, 'end-of-file')
    else:
        raise ParseError(t.lineno, t.value)

yacc.yacc(debug=1)
