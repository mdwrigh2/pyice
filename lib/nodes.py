import re
from jasmin_constants import init_jasmin, jasmin_types

class LabelGenerator(object):
    def __init__(self):
        self.i = 0

    def next(self):
        string = "label%d" % self.i
        self.i += 1
        return string

# Constants necessary for jasmin output

label = LabelGenerator()
className = ""

breakLabels = []

local_count = 0
fields = False

curr_proc = None

# End Constants

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
        return "invokestatic %s/read()I\n" % className

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

    def jasmin(self):
        
        string = self.lnode.jasmin()
        string += self.rnode.jasmin()
        if self.op == "+":
            string += "iadd\n"
        if self.op == "-":
            string += "isub\n"
        if self.op == "*":
            string += "imul\n"
        if self.op == "/":
            string += "idiv"

        return string

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
                string += "ldc 1\n"
                string += "goto %s\n" % l2
                string += "%s:\n" %l
                string += "ldc 0\n"
                string += "%s:\n" %l2
        else:
            # op is ?
            l = label.next() 
            l2 = label.next()
            string += "ifne %s\n" % l
            string += "ldc 0\n"
            string += "goto %s\n" % l2
            string += "%s:\n" % l
            string += "ldc 1\n"
            string += "%s:\n" %l2

        return string



class WriteNode(object):
    def __init__(self, op, child, lineno):
        self.op = op.lower()
        self.child = child
        if child.type == ('int', []) or child.type == ('string', []):
            self.type = None
        else:
            raise TypeError(lineno, 'incompatible type on write operation')

    def __str__(self):
        return "(%s %s)" % (self.op, self.child)

    def jasmin(self):
        string = self.child.jasmin()
        if self.child.type == ('int', []):
            string += "invokestatic %s/print(I)V\n" % className
        elif self.child.type == ('string', []):
            string += 'invokestatic %s/print(Ljava/lang/String;)V\n' % className
        if self.op == "write":
            string += 'ldc "\\n"\n'
            string += 'invokestatic %s/print(Ljava/lang/String;)V\n' % className

        return string


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

    def jasmin(self):
        string  = self.jasmin_reference()
        if self.var.type[0] == 'string':
            string += "aaload\n"
        else:
            string += "iaload\n"

        return string

    def jasmin_set(self):
        if self.var.type[0] == 'string':
            string = "aastore\n"
        else:
            string = "iastore\n"
        return string

    def jasmin_reference(self):
        if self.var.is_static:
            string = "getstatic %s/%s %s\n" % (className, self.var.name, jasmin_types(self.var.type))
        else:
            string = "aload %d\n" % self.var.local
        for i in self.indices[0:-1]:
            string += i.jasmin()
            string += "aaload\n"
        string += self.indices[-1].jasmin()
        return string
            


class VarNode(object):
    def __init__(self, type, name=None, val=None, is_writeable = True):
        self.type = type
        self.val = val
        self.name = name
        self.is_writeable = is_writeable
        self.local = -1
        self.is_static = False

    def __str__(self):
        string = "(VAR %s %s)" % (self.type, self.name)
        return string

    def jasmin(self):
        if self.is_static:
            string = "getstatic %s/%s %s\n" % (className, self.name, jasmin_types(self.type))
        else:
            if self.type == ('string', []):
                string = "aload %i\n" % self.local
            elif self.type == ('int', []):
                string = "iload %i\n" % self.local
            elif self.type == ('bool', []):
                string = "iload %i\n" % self.local
            else:
                raise TypeError(0, 'expected a basic type -- jasmin error')
        return string

    def jasmin_set(self):
        if self.is_static:
            string = "putstatic %s/%s %s\n" % (className, self.name, jasmin_types(self.type))
        else:
            if self.type == ('string', []):
                string = "astore %i\n" % self.local
            elif self.type == ('int', []):
                string = "istore %i\n" % self.local
            elif self.type == ('bool', []):
                string = "istore %i\n" % self.local
            else:
                raise TypeError(0, 'expected a basic type -- jasmin error')
        return string

    def jasmin_reference(self):
        return ""


class VarDeclNode(VarNode):
    def __init__(self, var):
        self.var = var

    def __str__(self):
        string = "(VAR-DECL %s %s)" % (self.var.type, self.var.name)
        return string

    def jasmin(self):
        if not curr_proc:
            self.var.is_static = True
            string = ".field public static %s %s\n" % (self.var.name, jasmin_types(self.var.type))
        else:
            global local_count
            s = local_count
            local_count += 1
            if self.var.type == ('bool', []) or self.var.type == ('int', []):
                string = "ldc 0\n"
                string += "istore %d\n" % (s)
            else:
                if self.var.type == ('string', []):
                    string = "aconst_null\n"
                else:
                    string = ""
                    for i in self.var.type[1]:
                        string += "bipush %d\n" % i
                    string += "multianewarray %s %d\n" % (jasmin_types(self.var.type), len(self.var.type[1]))
                string += "astore %d\n" % (s)
            self.var.local = s
        return string

    def jasmin_init(self):
        if self.var.type == ('bool', []) or self.var.type == ('int', []):
            string = "ldc 0\n"
        else:
            if self.var.type == ('string', []):
                string = "aconst_null\n"
            else:
                string = ""
                for i in self.var.type[1]:
                    string += "bipush %d\n" % i
                string += "multianewarray %s %d\n" % (jasmin_types(self.var.type), len(self.var.type[1]))

        string += "putstatic %s/%s %s\n" % (className, self.var.name, jasmin_types(self.var.type))
        return string



class ReturnNode(object):
    def __str__(self):
        return "(RETURN)"

    def jasmin(self):
        if not curr_proc or not curr_proc.ret_var:
            return "return\n"
        string = curr_proc.ret_var.jasmin()
        if curr_proc.ret == ('string', []):
            string += "areturn\n"
        else:
            string += "ireturn\n"

        return string

class BreakNode(object):
    def __str__(self):
        return "(BREAK)"

class ExitNode(object):
    def __str__(self):
        return "(EXIT)"

    def jasmin(self):
        return "iconst_1\ninvokestatic java/lang/System/exit(I)V\n"

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

    def jasmin(self):
        string = self.lnode.jasmin_reference()
        string += self.rnode.jasmin()
        string += self.lnode.jasmin_set()
        return string


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

    def jasmin(self):
        pass
        
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

    def jasmin(self):
        string = ""
        for s in self.stmts:
            string += s.jasmin()

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

    def __len__(self):
        return len(self.var_nodes)

    def jasmin_types(self):
        string = ""
        for v in self.var_nodes:
            string += jasmin_types(v.type)
        return string

    def setup(self):
        global local_count
        for v in self.var_nodes:
            v.local = local_count
            local_count += 1



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

    def jasmin(self):
        global local_count
        global curr_proc
        curr_proc = self
        local_count = 0
        self.declist.setup()
        if self.ret_var:
            self.ret_var.local = local_count
        local_count += 1
        string = ".method public static %s(%s)%s\n" % (self.name, self.declist.jasmin_types(), jasmin_types(self.ret))
        string += ".limit stack 100\n"
        jas_typevars = self.typevars.jasmin()
        jas_stms = self.stmts.jasmin()
        string += ".limit locals %d\n" % (local_count+len(self.declist)+2) # declist become the first n local variables, and 1 for padding
        string += jas_typevars
        string += jas_stms
        # This is because functions can have an implicit return
        string += ReturnNode().jasmin()
        string += ".end method\n"
        curr_proc = None
        return string

class ArgNode(object):
    def __init__(self, lineno):
        self.arg_nodes = []

    def prepend(self, node):
        self.arg_nodes = [node] + self.arg_nodes

    def __str__(self):
        string = "("
        for arg in self.arg_nodes:
            string += "(%s)" % arg
        string += ")"
        return string
    def jasmin(self):
        string = ""
        for arg in self.arg_nodes:
            string += arg.jasmin()
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
    def jasmin(self):
        return "; NULL\n"

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

    def jasmin(self):
        string = self.args.jasmin()
        string += "invokestatic %s/%s(%s)%s\n" % (className, self.proc.name, self.proc.declist.jasmin_types(), jasmin_types(self.proc.ret))
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

    def jasmin(self):
        string = ""
        for child in self.children:
            string += child.jasmin()
        return string


class ProgramNode(object):
    def __init__(self, begins, stms = None):
        self.begins = begins
        self.stms = stms

    def __str__(self):
        string = "(PROGRAM \n"
        string += "  BEGINS %s" % self.begins
        string += "\n  STMS %s" % self.stms
        return string

    def jasmin(self, cn, variables, functions):
        # This is a really terrible solution, but rather than sort the 
        # "begins" node into functions and variables, I'm just passing the
        # function dict in from after the parse. This sidesteps the problem of having
        # to ignore forwards (since they're function nodes missing the stmts),
        # and lets me output variables and then functions, which is necessary
        # according to the jasmin spec
        global className
        global fields
        className = cn
        # string = initial values, setup main
        string = init_jasmin(cn, variables)
        for f in functions.values():
            string += "%s \n ; END BEGINS \n" % f.jasmin()
        string += " .method public static main([Ljava/lang/String;)V \n.limit stack 100\n.limit locals 100\n"
        for v in variables.values():
            string += v.jasmin_init()
        if self.stms:
            string += "%s \n" % self.stms.jasmin()
        string += "return\n"
        string += ".end method\n"
        return string
