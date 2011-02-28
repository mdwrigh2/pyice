class SymbolTable():
    def __init__(self, default=None):
        if default == None:
            default = [{}]
        self.symbol_tables = default

    def lookup(self, var):
        for table in reversed(self.symbol_tables):
            if var in table:
                return table[var]

        raise SymbolLookupError(var)

    def lookup_top(self, var):
        table = self.symbol_tables[-1]
        return table.get(var, None)

    def lookup_not_top(self, var):
        tables = self.symbol_tables[0:-1]
        for table in reversed(tables):
            type = table.get(var, None)
            if not type:
                raise SymbolLookupError(var)
            else:
                return type
    
    def lookup_defaults(self,var):
        table = self.symbol_tables[0]
        type = table.get(var, None)
        if not type:
            raise SymbolLookupError(var)
        else:
            return type

    def push(self):
        self.symbol_tables.append({})

    def pop(self):
        self.symbol_tables.pop()

    def insert(self, var, node):
        if self.lookup_top(var):
            raise SymbolInsertionError(var)
        else:
            self.symbol_tables[-1][var] = node

    def insert_func(self, var, node):
        prev_node = self.lookup_top(var)
        if prev_node:
            if prev_node.stmts:
                raise ProcInsertionError("proc %s already defined" % var)
            elif prev_node.declist != node.declist:
                raise ProcInsertionError("Proc parameters does not agree with forward definition")
            elif prev_node.ret != node.ret:
                raise ProcInsertionError("Proc return values do not agree with forward definition")
            else:
                self.symbol_tables[-1][var] = node
        else:
            self.symbol_tables[-1][var] = node

    def insert_forward(self, var, node):
        if self.lookup_top(var):
            raise SymbolInsertionError(var)
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


class SymbolLookupError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "Symbol not found in symbol table: %s"  % self.value

class SymbolInsertionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Symbol already found in top scope: %s"  % self.value

class ProcInsertionError(SymbolInsertionError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
