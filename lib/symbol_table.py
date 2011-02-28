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
        if prev_node and prev_node.typevars:
            raise SymbolInsertionError(var)
        else:
            self.symbol_tables[-1][var] = node

    def insert_forward(self, var, node):
        if self.lookup_top(var):
            raise SymbolInsertionError(var)
        else:
            self.symbol_tables[-1][var] = node

    def __str__(self):
        return str(self.symbol_tables)

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

