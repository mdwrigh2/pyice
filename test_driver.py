import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import sys
fails = []

def test_result(b, fn):
    if b:
        sys.stdout.write('.')
    else:
        sys.stdout.write('F')
        fails.append('tests/'+fn)
    sys.stdout.flush()

for fn in os.listdir('tests'):
    if fn.endswith('.9') and not fn.startswith('.'):
        # Flush out the one before it
        sys.stdout.flush()
        for line in open('tests/'+fn, 'r'):
            if line.startswith('#:compile'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn], stdout = PIPE, stderr = STDOUT)
                test_result(retprocess == 0, fn)
            if line.startswith('#:error'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn], stdout = PIPE, stderr = STDOUT)
                test_result(retprocess != 0, fn)
sys.stdout.write('\n')
print "The following tests failed:"
for fail in fails:
    print fail
