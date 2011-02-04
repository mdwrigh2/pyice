import subprocess
from subprocess import Popen, PIPE, STDOUT
import os
import sys
fails = []
for fn in os.listdir('tests'):
    if fn.endswith('.9') and not fn.startswith('.'):
        for line in open('tests/'+fn, 'r'):
            if line.startswith('#:compile'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn], stdout = PIPE, stderr = STDOUT)
                if retprocess == 0:
                    sys.stdout.write('.')
                else:
                    fails.append('tests/'+fn)
                    sys.stdout.write('F')
            if line.startswith('#:error'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn], stdout = PIPE, stderr = STDOUT)
                if retprocess == 0:
                    fails.append('tests/'+fn)
                    sys.stdout.write('F')
                else:
                    sys.stdout.write('.')
sys.stdout.write('\n')
for fail in fails:
    print fail
