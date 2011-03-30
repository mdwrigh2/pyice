import re

class LabelGenerator(object):
    def __init__(self):
        self.i = 0

    def next(self):
        string = "label%d" % self.i
        self.i += 1
        return string

label = LabelGenerator()

class TypeError(Exception):
    def __init__(self, lineno, message):
        self.lineno = lineno
        self.message = message
    def __str__(self):
        return "line %d: %s" % (self.lineno, self.message)

class LitNode(object):
    def __init__(self, val, type, lineno):
        self.val = val
        self.type = type

    def __str__(self):
        return "(%s)" % (str(self.val))
    def jasmin(self):
        if self.type[0] == 'int':
            return "ldc %d\n" % self.val
        elif self.type[0] == 'string':
            return "ldc %s\n" % self.val
        else:
            if re.search(r"true", self.val, flags=re.IGNORECASE):
                return "ldc 1\n"
            else:
                return "ldc 0\n"


class ReadNode(object):
    def __init__(self, lineno):
        self.type = ('int', [])

    def __str__(self):
        return "(READ)"

    def jasmin(self):
        return "invokestatic %s.read()I" % className

class BinOpNode(object):
    def __str__(self):
        return "(%s %s %s)" % (self.op, self.lnode, self.rnode)

    def __init__(self, op, lnode, rnode, lineno):
        self.op = op
        self.lnode = lnode
        self.rnode = rnode
        if op == '+':
            if lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean or
                self.type = ('bool',[])
            elif lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '-':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '*':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            elif lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean and
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '/':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '%':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '!=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '>':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '<':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

        if op == '>=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')
        if op == '<=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(lineno, 'incompatible types to binary operator')

class UnaryOpNode(object):
    def __init__(self, op, child, lineno):
        self.op = op
        self.child = child
        if op == '-':
            if child.type == ('int', []):
                self.type = ('int', [])
            elif child.type == ('bool', []):
                self.type = ('bool', [])
            else:
                raise TypeError(lineno, 'incompatible types to unary operator')
        elif op == '?':
            if child.type == ('bool', []):
                self.type = ('int', [])
            else:
                raise TypeError(lineno, 'incompatible types to unary operator')

    def __str__(self):
        return "(%s %s)" % (self.op, self.child)

    def jasmin(self):
        string = self.child.jasmin()
        if self.op == "-":
            if self.type == ('int', []):
                string += "ineg\n"
                return string
            else:
                l = label.next() 
                l2 = label.next()
                string += "ifne %s\n" % l
                # need to finish this


class WriteNode(object):
    def __init__(self, op, child, lineno):
        self.op = op
        self.child = child
        if child.type == ('int', []) or child.type == ('string', []):
            self.type = None
        else:
            raise TypeError(lineno, 'incompatible type on write operation')

    def __str__(self):
        return "(%s %s)" % (self.op, self.child)

class ArrayNode(object):
    def __init__(self, var, indices, lineno):
        self.is_writeable = True
        self.var = var
        self.name = self.var.name
        self.indices = indices
        if len(var.type[1]) >= len(indices):
            self.var = var
            tmp = var.type[1][:]
            for i in indices:
                tmp.pop(0)
            self.type = (var.type[0], tmp)
        else:
            raise TypeError(lineno, 'attempted to access non-array object as array')
    def __str__(self):
        string = "("+self.name
        for i in self.indices:
            string += "[%s]" % (i)
        string += ")"
        return string


class VarNode(object):
    def __init__(self, type, name=None, val=None, is_writeable = True):
        self.type = type
        self.val = val
        self.name = name
        self.is_writeable = is_writeable
        self.location = -1
    def __str__(self):
        string = "(VAR %s %s)" % (self.type, self.name)
        return string

class VarDeclNode(VarNode):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        string = "(VAR-DECL %s %s)" % (self.var.type, self.var.name)
        return string

class ReturnNode(object):
    def __str__(self):
        return "(RETURN)"

class BreakNode(object):
    def __str__(self):
        return "(BREAK)"

class ExitNode(object):
    def __str__(self):
        return "(EXIT)"

class AssignNode(object):
    def __init__(self, lnode, rnode, lineno):
        self.lnode = lnode
        self.rnode = rnode
        self.lineno = lineno
        if len(lnode.type[1]) > 0:
            raise TypeError(lineno, 'cannot assign to array types')
        if lnode.type == rnode.type:
            if not self.lnode.is_writeable:
                raise TypeError(lineno, 'variable is not writable')
        else:
            raise TypeError(lineno, lnode.name)

    def __str__(self):
        return "(ASSIGN %s %s)" % (str(self.lnode), str(self.rnode))


class IfNode(object):
    def __init__(self, cond, then, elifs=None, els=None, lineno=0):
        self.cond = cond
        self.then = then
        if not elifs:
            elifs = []
        self.elifs = elifs
        self.els = els
        if cond.type == ('bool', []):
            pass
        else:
            raise TypeError(lineno, 'if')

    def __str__(self):
        string = "(IF %s THEN %s" % (self.cond, self.then)
        for e in self.elifs:
            string += "ELIF %s THEN %s" % (e.cond, e.then)

        if self.els:
            string += "ELSE %s" % (str(self.els))

        string += ")"
        return string
        
class StatementsNode(object):
    def __init__(self, stmt):
        self.stmts = [stmt]
    
    def append(self, stmt):
        self.stmts.append(stmt)

    def __str__(self):
        string = ""
        for s in self.stmts:
            string += str(s)+"\n"

        return string


class DoNode(object):
    def __init__(self, exp, then, lineno):
        self.exp = exp
        self.then = then
        if exp.type == ('bool', []):
            pass
        else:
            raise TypeError(lineno, 'do')

    def __str__(self):
        return "(WHILE %s DO %s)" % (str(self.exp), str(self.then))

class ForNode(object):
    def __init__(self,init_name, initial, final, stms = None, lineno = 0):
        if initial.type == ('int', []) and final.type == ('int', []):
            self.init_name = init_name
            self.initial = initial
            self.final = final
            self.stms = stms
        else:
            raise TypeError(lineno, 'fa')

    def __str__(self):
        return "(FOR %s FROM %s TO %s DO %s)" % (self.init_name, self.initial, self.final, self.stms)

class DecNode(object):
    def __init__(self, lineno):
        self.lineno = lineno
        self.var_nodes = []
    
    def append(self, var):
        self.var_nodes.append(var)

    def __eq__(self, other):
        if len(self.var_nodes) != len(other.var_nodes):
            return False
        else:
            for i in range(len(self.var_nodes)):
                if self.var_nodes[i].type != other.var_nodes[i].type:
                    return False
        return True
    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        string = "("
        for node in self.var_nodes:
            string += "(%s : %s) " % (node.name, node.type)

        string += ")"
        return string


class ProcNode(object):
    def __init__(self, name, declist, ret, ret_var, typevars, stmts, lineno):
        if not (ret == ('int', []) or ret == ('bool', []) or ret == ('string', []) or ret == ()):
            raise TypeError(lineno, 'proc %s does not return a basic type (int, bool, string).' % name)
        self.name = name
        self.declist = declist
        self.ret = ret
        self.ret_var = ret_var
        self.typevars = typevars
        self.stmts = stmts
        self.lineno = lineno

    def __str__(self):
        string = "(PROC (%s : %s) %s\n %s)" % (self.declist, self.ret,self.typevars, self.stmts)
        return string

class ArgNode(object):
    def __init__(self, lineno):
        self.arg_nodes = []

    def append(self, node):
        self.arg_nodes.append(node)

    def __str__(self):
        string = "("
        for arg in self.arg_nodes:
            string += "(%s)" % arg
        string += ")"
        return string


class NullNode(object):
    def __init__(self):
        self.type = ()
        self.val = None
        self.name = None

    def is_null(self):
        return True

    def __str__(self):
        return "()"

class CallNode(object):
    def __init__(self, proc, args, lineno):
        self.type = proc.ret
        self.proc = proc
        self.args = args
        self.lineno = lineno
        #if self.proc.stmts == None:
            #raise TypeError(lineno, 'function declared but not implemented')
        if len(proc.declist.var_nodes) != len(args.arg_nodes):
            raise TypeError(lineno, 'wrong number of arguments for function call')
        else:
            for i in range(len(args.arg_nodes)):
                if args.arg_nodes[i].type == proc.declist.var_nodes[i].type:
                    pass
                else:
                    raise TypeError(lineno, 'Incorrect type for function call')

    def __str__(self):
        string = "(CALL %s %s)" % (self.proc.name, self.args)
        return string

class Node(object):
    def __init__(self, children):
        self.children = children

    def __str__(self):
        string = "("
        for child in self.children:
            string += "(%s)\n" % (child)

        string += ")"
        return string
    
    def prepend(self, item):
        self.children = [item] + self.children

class ProgramNode(object):
    def __init__(self, begins, stms = None):
        self.begins = begins
        self.stms = stms

    def __str__(self):
        string = "(PROGRAM \n"
        string += "  BEGINS %s" % self.begins
        string += "\n  STMS %s" % self.stms
        return string
