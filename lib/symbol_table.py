class SymbolTable(object):
    def __init__(self, name, default=None):
        if default == None:
            default = [{}]
        self.symbol_tables = default
        self.name = name

    def lookup(self, var, line):
        for table in reversed(self.symbol_tables):
            if var in table:
                return table[var]

        raise SymbolLookupError(var,self.name,line)

    def lookup_top(self, var, line):
        table = self.symbol_tables[-1]
        return table.get(var, None, line)

    def lookup_not_top(self, var, line):
        tables = self.symbol_tables[0:-1]
        for table in reversed(tables):
            type = table.get(var, None)
            if not type:
                raise SymbolLookupError(var, self.name, line)
            else:
                return type
    
    def lookup_defaults(self,var, line):
        table = self.symbol_tables[0]
        type = table.get(var, None)
        if not type:
            raise SymbolLookupError(var, self.name, line)
        else:
            return type

    def push(self):
        self.symbol_tables.append({})

    def pop(self):
        self.symbol_tables.pop()

    def insert(self, var, node):
        if self.lookup_top(var, line):
            raise SymbolInsertionError(var, self.name, line)
        else:
            self.symbol_tables[-1][var] = node

    def __str__(self):
        return str(self.symbol_tables)

    def values(self):
        vals = []
        for table in self.symbol_tables:
            it = table.items()
            for i in it:
                vals.append(i[1])

        return vals

class FunctionTable(SymbolTable):
    def __init__(self, default=None):
        if default == None:
            default = [{}]
        self.symbol_tables = default
    def insert(self, var, node, line):
        prev_node = self.lookup_top(var, line)
        if prev_node:
            if prev_node.stmts:
                raise ProcInsertionError("Proc %s already defined", line)
            elif prev_node.declist != node.declist:
                raise ProcInsertionError("Proc parameters does not agree with forward definition", line)
            elif prev_node.ret != node.ret:
                raise ProcInsertionError("Proc return values do not agree with forward definition", line)
            else:
                self.symbol_tables[-1][var] = node
        else:
            self.symbol_tables[-1][var] = node

    def insert_forward(self, var, node, line):
        if self.lookup_top(var, line):
            raise ProcInsertionError('function already declared: %s' % var, line)
        else:
            self.symbol_tables[-1][var] = node

class SymbolLookupError(Exception):
    def __init__(self,value, name, line):
        self.value = value
        self.line = line
        self.name = name

    def __str__(self):
        return "line %d: %s not found in symbol table: %s"  % (self.line, self.name, self.value)

class SymbolInsertionError(Exception):
    def __init__(self, value, name, line):
        self.value = value
        self.line = line
        self.name = name

    def __str__(self):
        return "line %d: %s already found in top scope: %s"  % (self.line, self.name, self.value)

class ProcInsertionError(SymbolInsertionError):
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def __str__(self):
        return "line %d: %s" % (self.line, self.message)
