class TypeError(Exception):
    def __init__(self, lineno, message):
        self.lineno = lineno
        self.message = message
    def __str__(self):
        return "line %d: %s" % (self.lineno, repr(self.message))

class LitNode(object):
    def __init__(self, val, type, lineno):
        self.val = val
        self.type = type

class ReadNode(object):
    def __init__(self, lineno):
        self.type = ('int', [])

class BinOpNode(object):
    def __init__(self, op, lnode, rnode, lineno):
        self.type = 'BinOpNode'
        if op == '+':
            if lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean or
                self.type = ('bool',[])
            elif lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, op)

        if op == '-':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, op)

        if op == '*':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            elif lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean and
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

        if op == '/':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, op)

        if op == '%':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, op)

        if op == '=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

        if op == '!=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

        if op == '>':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

        if op == '<':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

        if op == '>=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)
        if op == '<=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, op)

class UnaryOpNode(object):
    def __init__(self, op, child, lineno):
        if op == '-':
            if child.type == ('int', []):
                self.type = ('int', [])
            else:
                raise TypeError(lineno, op)
        elif op == '?':
            if child.type == ('bool', []):
                self.type = ('bool', [])
            else:
                raise TypeError(lineno, op)

class WriteNode(object):
    def __init__(self, op, child, lineno):
        if child.type == ('int', []) or child.type == ('string', []):
            self.type = None
        else:
            raise TypeError(lineno, op)

class AssignNode(object):
    pass

class ArrayNode(object):
    def __init__(self, var, indices, lineno):
        if len(var.type[1]) >= len(indices):
            self.var = var
            tmp = var.type[1]
            for i in indices:
                tmp.pop(0)
            self.type = (var.type[0], tmp)
        else:
            raise TypeError(lineno, var.name)

class VarNode(object):
    def __init__(self, type, name=None, val=None):
        self.type = type
        self.val = val
        self.name = name

class ReturnNode(object):
    pass

class BreakNode(object):
    pass

class ExitNode(object):
    pass

class AssignNode(object):
    def __init__(self, lnode, rnode, lineno):
        if lnode.type == rnode.type:
            pass
        else:
            raise TypeError(lineno, lnode.name)

class IfNode(object):
    def __init__(self, cond, then, elifs=None, els=None, lineno=0):
        if cond.type == ('bool', []):
            pass
        else:
            raise TypeError(lineno, 'if')
        
class StatementsNode(object):
    def __init__(self, stmt):
        self.stmts = [stmt]
    
    def append(self, stmt):
        self.stmts.append(stmt)

class DoNode(object):
    def __init__(self, exp, then, lineno):
        if exp.type == ('bool', []):
            pass
        else:
            raise TypeError(lineno, 'do')

class ForNode(object):
    def __init__(self, initial, final, stmts = None, lineno = 0):
        if initial.type == ('int', []) and final.type == ('int', []):
            pass
        else:
            raise TypeError(lineno, 'fa')

class DecNode(object):
    def __init__(self, lineno):
        self.lineno = lineno
        self.var_nodes = []
    
    def append(self, var):
        self.var_nodes.append(var)

class ProcNode(object):
    def __init__(self, name, declist, ret, typevars, stmts):
        #implement this
        # also go back and implement all of the statements that are null. you may need them
        # particularly typevars
        pass

class NullNode(object):
    def __init__(self):
        self.type = None
        self.val = None
        self.name = None
