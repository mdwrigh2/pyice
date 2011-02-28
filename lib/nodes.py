class TypeError(Exception):
    def __init__(self, lineno, token):
        self.lineno = lineno
        self.token = token

class LitNode(object):
    def __init__(self, val, type):
        self.val = val
        self.type = type

class BinOpNode(object):
    def __init__(self, op, lnode, rnode):
        self.type = 'BinOpNode'
        if op == '+':
            if lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean or
                self.type = ('bool',[])
            elif lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '-':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '*':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            elif lnode.type == ('bool',[]) and rnode.type == ('bool',[]):
                # Boolean and
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '/':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '%':
            if lnode.type == ('int',[]) and rnode.type == ('int',[]):
                self.type = ('int',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '!=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])) or (lnode.type == ('bool',[]) and rnode.type == ('bool',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '>':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '<':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

        if op == '>=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])
        if op == '<=':
            if (lnode.type == ('int',[]) and rnode.type == ('int',[])):
                self.type = ('bool',[])
            else:
                raise TypeError(t.lineno(2), t[2])

class UnaryOpNode(object):
    def __init__(self, op, child):
        if op == '-':
            if child.type == ('int', []):
                self.type = ('int', [])
            else:
                raise TypeError(t.lineno(1), t[1])
        elif op == '?':
            if child.type == ('bool', []):
                self.type = ('bool', [])
            else:
                raise TypeError(t.lineno(1), t[1])


