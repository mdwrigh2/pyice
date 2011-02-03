import subprocess
import os
import sys

for fn in os.listdir('tests'):
    if fn.endswith('.9') and not fn.startswith('.'):
        for line in open('tests/'+fn, 'r'):
            if line.startswith('#:compile'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn])
                if retprocess ==0:
                    sys.stdout.write('.')
                else:
                    sys.stdout.write('F')
            if line.startswith('#:error'):
                retprocess = subprocess.call(['./ice9', 'tests/'+fn])
                if retprocess == 0:
                    sys.stdout.write('F')
                else:
                    sys.stdout.write('.')
