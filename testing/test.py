#!/usr/bin/env python

# INSTRUCTIONS
# ============
#
# This is a test suite for ICE9 compilers.
#
# This program must be run from the directory where "tests" is. Your compiler
# will be run like this: (change as necessary)
COMPILER_EXE = './ice9'

# Your compiler should:
# - Read the input program from standard input.
# - Return 0 on success and nonzero on error.
# - Print a line number when any error occurs
# - When a syntax error occurs, print the first token that could not be part of
#   a valid program.
# If you don't want to check the contents of error messages, set this to False.
CHECK_ERROR_CONTENTS = True

# Only the most basic parts of error messages are tested; you'll need to check
# your messages yourself.

# TEST FILE FORMAT
# ================
#
# Each program in tests/ has a comment indicating the expected result of
# compiling it. The comment can have one of the following formats:
#
#:compile
# This means the program should compile successfully.
#
#:error 3, "[]", ";"
# This means there should be an error on line 3, and the error message should
# contain both "[]" and ";" (strings in JSON format). Both the line number and
# strings are optional.
#
#:unknown
# This means behavior is implementation-dependent, but the compiler shouldn't
# crash.

from subprocess import Popen, PIPE, STDOUT
from json import loads as load_json
import unittest

class ICE9Test(unittest.TestCase):
    def __init__(self, fn):
        unittest.TestCase.__init__(self)
        self.fn = fn

    def runTest(self):
        with open(self.fn, 'rb') as f:
            compiler = Popen([COMPILER_EXE], stdin = f, stdout = PIPE, stderr = STDOUT)
            output = compiler.communicate()[0].decode('latin-1').strip()
            if compiler.returncode == -11: # SIGSEGV
                self.fail('Compiler segfaulted')
            elif compiler.returncode < 0:
                self.fail('Compiler terminated with signal %d'%(compiler.returncode))

            seenDirective = False
            f.seek(0)
            for line in f:
                line = line.decode('latin-1')
                if not line.startswith('#:'):
                    continue
                seenDirective = True
                if line.startswith('#:error'):
                    if not compiler.returncode:
                        self.fail('Compile incorrectly succeeded')
                    words = load_json('['+line[7:].strip()+']')
                    if not CHECK_ERROR_CONTENTS:
                        if len(words) > 0 and type(words[0]) == int:
                            words = words[:1]
                        else:
                            words = []
                    for word in words:
                        self.assertIn(str(word), output)
                elif line.startswith('#:compile'):
                    if compiler.returncode:
                        self.fail('Compile failed: ' + repr(output))
                elif line.startswith('#:unknown'):
                    pass
                else:
                    self.fail('Unrecognized test directive ' + repr(line))
            if not seenDirective:
                self.fail('No test directive')

    def __str__(self):
        return self.fn

class FakeLoader(object):
    def loadTestsFromModule(self, *args, **kwargs):
        import os
        return unittest.TestSuite(ICE9Test('tests/'+fn) for fn in os.listdir('tests') if fn.endswith('.9') and not fn.startswith('.'))

if __name__ == '__main__':
    unittest.main(testLoader = FakeLoader())
