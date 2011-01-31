import yacc

import pyice_parser

import sys

class Compiler:

    def _parse(self):
        self.ast = yacc.parse(self.code)

    def compile(self, code):
        self.code = code
        print self._parse()


def start_compiler():
    files = sys.argv[1:]

    for file in files:
        source = open(file, 'r')
        code = source.read()
        source.close
        print Compiler().compile(code)

if __name__ == '__main__':
    start_compiler()
