#!/usr/bin/env python
import subprocess
from subprocess import PIPE, STDOUT
import os
import sys
fails = []

file_dir = sys.argv[1]


def test_result(b, fn):
    if b:
        sys.stdout.write('\033[92m.')
    else:
        sys.stdout.write('\033[91mF')
        fails.append(file_dir+'/'+fn)
    sys.stdout.flush()

for fn in os.listdir(file_dir):
    if fn.endswith('.9') and not fn.startswith('.'):
        # Flush out the one before it
        sys.stdout.flush()
        for line in open(file_dir+'/'+fn, 'r'):
            if line.startswith('#:compile'):
                retprocess = subprocess.call(['../ice9', file_dir+'/'+fn], stdout = PIPE, stderr = STDOUT)
                test_result(retprocess == 0, fn)
            if line.startswith('#:error'):
                retprocess = subprocess.call(['../ice9', file_dir+'/'+fn], stdout = PIPE, stderr = STDOUT)
                test_result(retprocess != 0, fn)
sys.stdout.write('\n\n')
if fails:
    print "\033[91mThe following tests failed:"
    for fail in fails:
        print fail
else:
    print "All tests passed!\033[0m"
    
