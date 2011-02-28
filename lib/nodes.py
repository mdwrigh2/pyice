class TypeError(Exception):
    def __init__(self, lineno, token):
        self.lineno = lineno
        self.token = token
    def __str__(self):
        return repr(self.token)

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

